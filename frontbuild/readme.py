"""Read warehouse dataset READMEs and write the front repo's dataset/lens READMEs."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .tables import CleanTable

WAREHOUSE_WEB = "https://github.com/sarveshkant2003-afk/bharatnomy-data"

# Unit from the column-name suffix (warehouse convention: "the unit is in the column name").
# Longest suffix first.
UNIT_SUFFIXES = [
    ("_000_ha", "thousand hectares"), ("_mm_day", "mm/day"), ("_w_m2", "W/m²"), ("_sq_km", "km²"),
    ("_pct", "%"), ("_ha", "hectares"), ("_mm", "mm"), ("_ms", "m/s"), ("_kt", "knots"),
    ("_km", "km"), ("_frac", "fraction (0-1)"), ("_inr", "₹"), ("_tpd", "tonnes/day"), ("_c", "°C"),
]


def unit_from_name(column: str) -> str:
    for suffix, unit in UNIT_SUFFIXES:
        if column.endswith(suffix):
            return unit
    return ""


@dataclass
class WarehouseReadme:
    title: str
    summary: str  # first paragraph under the title
    sections: dict[str, str]  # "Source", "Notes", ... -> body (markdown)
    # (column patterns, description, from the column cell itself?) Patterns that only
    # appear inside a description (e.g. `main_cultivators_*`) are tried last.
    column_docs: list[tuple[list[str], str, bool]]

    def describe(self, column: str, all_columns: list[str]) -> str:
        """Description for a column, trying exact names, wildcards, ranges, then mentions."""
        for primary_only in (True, False):
            for patterns, text, is_primary in self.column_docs:
                if is_primary != primary_only:
                    continue
                if any(_pattern_matches(p, column, patterns[0], all_columns) for p in patterns):
                    return text
        return ""


def _pattern_matches(pattern: str, column: str, first: str, all_columns: list[str]) -> bool:
    if " ... " in pattern:
        # "`forests_ha` ... `fallow_land_total_ha`": every column between the two, in file order.
        start, end = pattern.split(" ... ")
        if start in all_columns and end in all_columns:
            i, j = all_columns.index(start), all_columns.index(end)
            return column in all_columns[i : j + 1]
        return False
    if "*" in pattern or "<" in pattern or pattern.startswith("..."):
        regex = re.escape(pattern)
        regex = re.sub(r"<[^>]+>", ".+", regex.replace(r"\<", "<").replace(r"\>", ">"))
        regex = regex.replace(r"\*", ".+").replace(r"\.\.\.", ".*")
        return re.fullmatch(regex, column) is not None
    if pattern.startswith("_"):
        # "`fire_detections_jan_feb`, `_mar_may`": a suffix of the first column's stem.
        stem = first.split("_")[0]
        return column.startswith(stem) and column.endswith(pattern)
    return pattern == column


def parse_readme(path: Path, folder: str, sha: str) -> WarehouseReadme:
    text = _absolute_links(path.read_text(encoding="utf-8"), folder, sha)
    title_match = re.search(r"^# (.+)$", text, re.M)
    title = title_match.group(1).strip() if title_match else folder
    body = text[title_match.end():] if title_match else text
    summary = body.strip().split("\n\n")[0].strip()
    sections = {
        m.group(1).strip(): m.group(2).strip()
        for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    }
    docs: list[tuple[list[str], str, bool]] = []
    for line in sections.get("Columns", "").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and len(cells) >= 2 and "`" in cells[0]:
            # Join "`a` ... `b`" into one range pattern before splitting on backticks.
            col_cell = re.sub(r"`([^`]+)`\s*\.\.\.\s*`([^`]+)`", r"`\1 ... \2`", cells[0])
            docs.append((re.findall(r"`([^`]+)`", col_cell), cells[1], True))
            mentioned = [t for t in re.findall(r"`([^`]+)`", cells[1]) if "*" in t]
            if mentioned:
                docs.append((mentioned, cells[1], False))
    # Bullets anywhere in the README: "- `column`: description"
    for m in re.finditer(r"^\s*- `([^`]+)`: (.+)$", text, re.M):
        docs.append(([m.group(1)], m.group(2).strip(), True))
    return WarehouseReadme(title, summary, sections, docs)


def _absolute_links(text: str, folder: str, sha: str) -> str:
    """Relative links in a warehouse README point into the warehouse; pin them to the commit."""
    def fix(m: re.Match[str]) -> str:
        target = m.group(2)
        if re.match(r"^(https?:|mailto:|#)", target):
            return m.group(0)
        path = target[3:] if target.startswith("../") else f"{folder}/{target}"
        return f"{m.group(1)}({WAREHOUSE_WEB}/tree/{sha}/{path})"
    return re.sub(r"(\[[^\]]*\])\(([^)\s]+)\)", fix, text)


def _cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def dataset_readme(table: CleanTable, docs: list[WarehouseReadme], state_name: str,
                   n_state_districts: int, json_file: str, sha: str) -> tuple[str, list[str]]:
    """Markdown for one dataset folder. Returns (text, columns with no description)."""
    name = str(table.plan.output_name)
    newest = docs[-1]
    df = table.data
    derived_names = {d["new_column"]: d for d in table.derived}
    districts = sorted(set(df["district"]))
    title = newest.title.replace(", India,", ",")  # the file is one state now
    lines = [f"# {title} — {state_name}", "", newest.summary, ""]

    lines += ["## Coverage", ""]
    lines.append(f"- **Rows:** {len(df):,}")
    lines.append(f"- **Period:** {table.plan.output_name.period.replace('-to-', ' to ')}")
    if table.period_note:
        lines.append(f"- **Note:** {table.period_note}")
    lines.append(f"- **Districts:** {len(districts)} of {n_state_districts}"
                 + (f" ({', '.join(districts)})" if len(districts) <= 5 else ""))
    if table.state_total_rows_dropped:
        lines.append(f"- {table.state_total_rows_dropped} state-total row(s) from the warehouse table are left out; add up district rows instead.")
    if len(table.plan.parts) > 1:
        lines.append(f"- Merged from {len(table.plan.parts)} warehouse tables split by period.")
    if json_file.endswith(".jsonl"):
        lines.append(f"- JSON is in **JSON Lines** format (`{json_file}`, one object per line) because it is large.")
    lines.append("")

    for doc_section in ("Source", "How it is computed"):
        for d in docs:
            if doc_section in d.sections and (doc_section != "How it is computed" or table.plan.output_name.source == "BNY"):
                heading = doc_section if len(docs) == 1 else f"{doc_section} ({_part_period(d, table)})"
                lines += [f"## {heading}", "", d.sections[doc_section], ""]
    if table.plan.output_name.source == "BNY" and not any("How it is computed" in d.sections for d in docs):
        lines += ["## Bharatnomy calculation", "", "This table is computed by Bharatnomy, not published as-is by the source. See the notes below.", ""]

    lines += ["## Columns", "", "| Column | Type | Unit | Description |", "|---|---|---|---|"]
    undocumented: list[str] = []
    for col in df.columns:
        if col in derived_names:
            rule = derived_names[col]
            desc = f"**derived**: {rule['description']} (`{rule['formula']}`)"
            unit = rule["unit"]
        else:
            desc = next((d.describe(col, list(df.columns)) for d in reversed(docs)
                         if d.describe(col, list(df.columns))), "")
            unit = unit_from_name(col)
            if not desc:
                undocumented.append(col)
        lines.append(f"| `{col}` | {table.types.get(col, 'text')} | {_cell(unit)} | {_cell(desc)} |")
    lines += ["", "Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.", ""]

    if "Notes" in newest.sections:
        lines += ["## Notes from the warehouse", "", "These describe the full warehouse table (all states).", "", newest.sections["Notes"], ""]

    lines += ["## Where this comes from", ""]
    for part in table.plan.parts:
        lines.append(f"- Warehouse folder [`{part}`]({WAREHOUSE_WEB}/tree/{sha}/{part}) at commit `{sha[:12]}`")
    lines += [f"- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `{name}.csv`, `{json_file}`.", ""]
    return "\n".join(lines), undocumented


def _part_period(doc: WarehouseReadme, table: CleanTable) -> str:
    # Titles usually end with the period; fall back to the title itself.
    return doc.title.split(",")[-1].strip()


def lens_readme(lens_name: str, state_name: str, rows: list[tuple[str, str, str, int]]) -> str:
    """rows: (dataset name, title, period, row count)."""
    lines = [f"# {lens_name} — {state_name}", ""]
    if not rows:
        return "\n".join(lines + ["No district-level data for this lens yet.", ""])
    lines += ["| Dataset | What it holds | Period | Rows |", "|---|---|---|---|"]
    for name, title, period, n in rows:
        lines.append(f"| [`{name}`]({name}/) | {_cell(title)} | {period.replace('-to-', ' to ')} | {n:,} |")
    return "\n".join(lines + [""])
