"""Turn warehouse table(s) into one clean, state-filtered table.

All values stay as strings the whole way through, so nothing is rounded or
re-formatted by accident. Column *types* (text / integer / number) are worked out
separately and only used when writing JSON.

Order of steps (see CLAUDE.md, "Per-dataset processing"):
read -> filter to state -> clean -> fix district codes -> merge parts -> derived columns -> sort.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from .config import Reference, State, read_text_csv
from .discover import DatasetPlan
from .naming import make_period, period_bounds
from .report import Report

# Cells that mean "no value". They become empty (CSV) / null (JSON).
MISSING_TOKENS = {"NA", "N/A", "NaN", "nan", "null", "NULL", "None"}
# Columns that are always text, even when they look like numbers.
TIME_COLUMNS = ["year", "period", "month", "date"]
ALWAYS_TEXT = set(TIME_COLUMNS) | {"state_ut", "district"}

NUMBER_RE = re.compile(r"^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$")
INTEGER_RE = re.compile(r"^[+-]?\d+$")
THOUSANDS_RE = re.compile(r"^-?\d{1,3}(,\d{3})+(\.\d+)?$")


@dataclass
class CleanTable:
    """A finished table plus the facts its README and checks need."""

    plan: DatasetPlan
    data: pd.DataFrame  # all strings, '' = missing
    types: dict[str, str]  # column -> "text" | "integer" | "number"
    warehouse_rows: int  # rows for this state across all parts, before dropping anything
    state_total_rows_dropped: int = 0
    merge_duplicates_dropped: int = 0
    merge_conflicts_dropped: int = 0
    period_note: str = ""
    derived: list[dict[str, str]] = field(default_factory=list)


def is_text_column(name: str) -> bool:
    return name in ALWAYS_TEXT or name.endswith("_code") or name.startswith("lgd_")


# ---------- reading and cleaning ----------

def read_part(warehouse: Path, folder: str) -> pd.DataFrame:
    path = warehouse / folder / f"{folder}.csv"
    return read_text_csv(path)


def trim_and_blank(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """Trim whitespace and turn missing-value tokens into ''. Returns (df, cells blanked)."""
    df = df.apply(lambda col: col.str.strip())
    is_token = df.isin(sorted(MISSING_TOKENS))
    return df.mask(is_token, ""), int(is_token.to_numpy().sum())


def strip_thousands(df: pd.DataFrame, types: dict[str, str]) -> int:
    """Remove thousands separators ('1,234' -> '1234') in number columns, in place."""
    changed = 0
    for col, kind in types.items():
        if kind == "text":
            continue
        hits = df[col].str.match(THOUSANDS_RE)
        if hits.any():
            df.loc[hits, col] = df.loc[hits, col].str.replace(",", "", regex=False)
            changed += int(hits.sum())
    return changed


def infer_types(df: pd.DataFrame) -> dict[str, str]:
    """text / integer / number for each column, judged on the whole warehouse table."""
    types: dict[str, str] = {}
    for col in df.columns:
        values = df[col][df[col] != ""]
        # Allow '1,234' here; strip_thousands removes the commas afterwards.
        values = values.str.replace(r"(?<=\d),(?=\d{3}\b)", "", regex=True)
        if is_text_column(col) or values.empty or not values.str.match(NUMBER_RE).all():
            types[col] = "text"
        elif values.str.match(INTEGER_RE).all():
            types[col] = "integer"
        else:
            types[col] = "number"
    return types


def combine_types(a: dict[str, str], b: dict[str, str]) -> dict[str, str]:
    """Merge column types from several parts: text beats number beats integer."""
    rank = {"integer": 0, "number": 1, "text": 2}
    out = dict(b)
    for col, kind in a.items():
        if col in out and rank[kind] > rank[out[col]]:
            out[col] = kind
    return out


def normalise_time(df: pd.DataFrame, report: Report, label: str) -> None:
    """Make dates ISO, months YYYY-MM, financial years YYYY-YY; report anything unrecognised."""
    rules = {
        # column: list of (pattern, replacement); the final pattern is the accepted form
        "date": [(r"^(\d{2})[-/](\d{2})[-/](\d{4})$", r"\3-\2-\1"), (r"^(\d{4})/(\d{2})/(\d{2})$", r"\1-\2-\3")],
        "month": [(r"^(\d{4})-(\d)$", r"\1-0\2")],
        "year": [],
    }
    accepted = {
        "date": r"^\d{4}-\d{2}-\d{2}$",
        "month": r"^\d{4}-\d{2}$",
        "year": r"^\d{4}(-\d{2})?$",
    }
    for col, subs in rules.items():
        if col not in df:
            continue
        before = df[col].copy()
        for pattern, repl in subs:
            df[col] = df[col].str.replace(pattern, repl, regex=True)
        if col == "year":
            # 2010-2011 -> 2010-11, only when the years are consecutive.
            df[col] = df[col].map(_short_financial_year)
        changed = int((before != df[col]).sum())
        if changed:
            report.add("Cleaning", f"`{label}`: reformatted {changed} `{col}` values")
        bad = df[col][(df[col] != "") & ~df[col].str.match(accepted[col])]
        if len(bad):
            report.add("Cleaning", f"`{label}`: {len(bad)} `{col}` values not in standard form, left as is (e.g. `{bad.iloc[0]}`)")


def _short_financial_year(value: str) -> str:
    m = re.match(r"^(\d{4})-(\d{4})$", value)
    if m and int(m.group(2)) == int(m.group(1)) + 1:
        return f"{m.group(1)}-{m.group(2)[2:]}"
    return value


# ---------- districts ----------

def _name_index(districts: pd.DataFrame) -> dict[str, str]:
    """Lower-case name/alias -> lgd_district_code, for the name fallback."""
    index: dict[str, str] = {}
    for row in districts.to_dict("records"):
        names = [row["district"], row["census2011_name"], *row["aliases"].split(";")]
        for name in names:
            if name.strip():
                index[name.strip().lower()] = row["lgd_district_code"]
    return index


def fix_districts(df: pd.DataFrame, state: State, ref: Reference, report: Report, label: str) -> tuple[pd.DataFrame, int]:
    """Fill missing codes by name fallback, drop state-total rows, standardise names.

    Returns (df, number of state-total rows dropped).
    """
    districts = ref.districts(state.lgd_state_code)
    code_to_name = dict(zip(districts["lgd_district_code"], districts["district"]))
    dropped = 0
    blank = df["lgd_district_code"] == ""
    if blank.any():
        index = _name_index(districts)
        for i in df.index[blank]:
            name = df.at[i, "district"]
            code = index.get(name.lower())
            if code:
                df.at[i, "lgd_district_code"] = code
                report.add("Name-fallback matches", f"`{label}`: `{name}` → {code} ({code_to_name[code]})")
        still_blank = df["lgd_district_code"] == ""
        dropped_names = sorted(df.loc[still_blank, "district"].unique())
        for name in dropped_names:
            if "total" not in name.lower():
                report.add("Errors", f"`{label}`: dropped row(s) with no district code that do not look like a total: `{name}`")
        dropped = int(still_blank.sum())
        if dropped:
            report.add("State-total rows dropped", f"`{label}`: {dropped} row(s) ({', '.join(f'`{n}`' for n in dropped_names)})")
        df = df.loc[~still_blank]
    unknown = sorted(set(df["lgd_district_code"]) - set(code_to_name))
    if unknown:
        report.add("Errors", f"`{label}`: lgd_district_code not in geography.csv for this state: {unknown}")
    df = df.copy()
    df["district"] = df["lgd_district_code"].map(code_to_name).fillna(df["district"])
    return df, dropped


# ---------- merging parts ----------

def merge_parts(parts: list[pd.DataFrame], types: dict[str, str], report: Report, label: str) -> tuple[pd.DataFrame, int, int]:
    """Concatenate period parts (oldest first). Returns (df, exact duplicates, conflicts dropped)."""
    columns = list(parts[0].columns)
    for p in parts[1:]:
        if list(p.columns) != columns:
            raise ValueError(f"{label}: parts have different columns; cannot merge")
    df = pd.concat(parts, ignore_index=True)
    before = len(df)
    df = df.drop_duplicates()
    exact = before - len(df)
    # Same key (all text columns) but different numbers = conflict. Keep the newer part (last).
    key = [c for c in columns if types[c] == "text"]
    conflict_mask = df.duplicated(subset=key, keep="last")
    conflicts = int(conflict_mask.sum())
    if conflicts:
        sample = df.loc[conflict_mask, key].head(3).to_dict("records")
        report.add("Merges", f"`{label}`: {conflicts} overlapping row(s) with conflicting values; kept the newer part. e.g. {sample}")
    if exact:
        report.add("Merges", f"`{label}`: dropped {exact} exact duplicate row(s)")
    return df.loc[~conflict_mask], exact, conflicts


# ---------- derived columns ----------

def add_derived(df: pd.DataFrame, rules: pd.DataFrame, types: dict[str, str], label: str) -> list[dict[str, str]]:
    """Add the columns config/derived_columns.csv lists for this dataset (in place)."""
    added: list[dict[str, str]] = []
    for rule in rules[rules["dataset"] == label].to_dict("records"):
        numeric = df.apply(lambda col: pd.to_numeric(col.where(col != ""), errors="coerce") if types.get(col.name) != "text" else col)
        values = numeric.eval(rule["formula"])
        # Fixed formatting (max 4 decimals) keeps output deterministic.
        df[rule["new_column"]] = values.map(lambda v: "" if pd.isna(v) else f"{v:.4f}".rstrip("0").rstrip("."))
        types[rule["new_column"]] = "number"
        added.append(rule)
    return added


# ---------- sorting and period ----------

def sort_rows(df: pd.DataFrame, types: dict[str, str]) -> pd.DataFrame:
    """LGD district code (as a number), then time columns, then other text keys, then the rest."""
    time_cols = [c for c in TIME_COLUMNS if c in df]
    other_keys = [c for c in df.columns if types.get(c) == "text" and c not in time_cols
                  and c not in ("lgd_district_code", "district", "state_ut", "lgd_state_code")]
    rest = [c for c in df.columns if c not in time_cols + other_keys]
    df = df.assign(_code=df["lgd_district_code"].astype(int))
    df = df.sort_values(["_code", *time_cols, *other_keys, *rest], kind="stable", key=_natural_key)
    return df.drop(columns="_code").reset_index(drop=True)


def _natural_key(col: pd.Series) -> pd.Series:
    """Sort '2' before '10' in text columns by zero-padding every run of digits."""
    if col.name == "_code":
        return col
    return col.astype(str).str.replace(r"\d+", lambda m: m.group(0).zfill(12), regex=True)


def actual_period(df: pd.DataFrame, name_period: str) -> tuple[str, str]:
    """Period for the output name from the state's own `year` values. Returns (period, note)."""
    if "year" not in df or (df["year"] == "").all():
        return name_period, ""
    years = df["year"][df["year"] != ""]
    period = make_period(years.min(), years.max())
    if period_bounds(period) == period_bounds(name_period):
        return name_period, ""
    return period, f"The warehouse table covers {name_period}; this state's rows cover {period}."


# ---------- one dataset, end to end ----------

def build_table(warehouse: Path, plan: DatasetPlan, state: State, ref: Reference,
                derived_rules: pd.DataFrame, report: Report) -> CleanTable:
    label = str(plan.output_name)
    cleaned: list[pd.DataFrame] = []
    types: dict[str, str] = {}
    warehouse_rows = dropped = 0
    for folder in plan.parts:
        raw, _ = trim_and_blank(read_part(warehouse, folder))
        types = combine_types(types, infer_types(raw))  # judged on all states
        part = raw[raw["lgd_state_code"] == state.lgd_state_code].copy()
        warehouse_rows += len(part)
        commas = strip_thousands(part, types)
        if commas:
            report.add("Cleaning", f"`{folder}`: removed thousands separators from {commas} cells")
        normalise_time(part, report, folder)
        part, n = fix_districts(part, state, ref, report, folder)
        dropped += n
        cleaned.append(part)
    if len(cleaned) > 1:
        df, exact, conflicts = merge_parts(cleaned, types, report, label)
    else:
        df, exact, conflicts = cleaned[0], 0, 0
    derived = add_derived(df, derived_rules, types, label)
    df = sort_rows(df, types)
    period, period_note = actual_period(df, plan.output_name.period)
    if period_note:
        plan.output_name = plan.output_name.with_period(period)
        label = str(plan.output_name)
        report.add("Cleaning", f"`{label}`: {period_note}")
    text_numbers = [c for c, t in types.items() if t == "text" and not is_text_column(c)
                    and (df[c] != "").any() and df[c].str.match(NUMBER_RE).mean() > 0.5]
    if text_numbers:
        report.add("Column types", f"`{label}`: mostly-numeric columns kept as text because some cells are not numbers: {text_numbers}")
    return CleanTable(plan=plan, data=df, types=types, warehouse_rows=warehouse_rows,
                      state_total_rows_dropped=dropped, merge_duplicates_dropped=exact,
                      merge_conflicts_dropped=conflicts, period_note=period_note, derived=derived)
