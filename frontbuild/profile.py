"""Build district-profile.csv/.json: one row per district, one value per indicator.

Indicators come from config/profile_indicators.csv. For each indicator we take the
built (clean) table, apply its optional filter, and pick one value per district:
  latest = the row with the latest time value that district has.
Every indicator gets two columns: <indicator_id> and <indicator_id>_year.
A district with no value gets an empty cell (null in JSON), never a zero.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .config import Reference, State
from .naming import DatasetName
from .report import Report
from .tables import TIME_COLUMNS, CleanTable, _natural_key
from .writers import write_csv, write_json

AGGREGATIONS = {"latest"}


def _latest(df: pd.DataFrame, column: str, period: str) -> pd.DataFrame:
    """One row per district: lgd_district_code, value, year."""
    time_col = next((c for c in TIME_COLUMNS if c in df and (df[c] != "").any()), None)
    df = df[df[column] != ""]
    if time_col is None:
        # No time column (e.g. a single Census year): the period comes from the dataset name.
        out = df[["lgd_district_code", column]].assign(year=period)
    else:
        df = df.assign(_t=_natural_key(df[time_col]))
        latest_t = df.groupby("lgd_district_code")["_t"].transform("max")
        out = df[df["_t"] == latest_t][["lgd_district_code", column, time_col]].rename(columns={time_col: "year"})
    return out.rename(columns={column: "value"})


def build_profile(tables: dict[str, CleanTable], state: State, ref: Reference,
                  indicators: pd.DataFrame, state_dir: Path, report: Report) -> None:
    districts = ref.districts(state.lgd_state_code)
    profile = districts[["lgd_district_code", "district"]].copy()
    profile = profile.assign(_code=profile["lgd_district_code"].astype(int)).sort_values("_code").drop(columns="_code")
    types: dict[str, str] = {"lgd_district_code": "text", "district": "text"}

    for ind in indicators.to_dict("records"):
        iid, name, column = ind["indicator_id"], ind["dataset"], ind["column"]
        aggregation = ind["aggregation"] or "latest"
        # Indicators name datasets with one state's code (e.g. _MH_); use this state's version.
        name = str(DatasetName.parse(name).with_geography(state.code_short))
        table = tables.get(name)
        problem = (
            f"dataset `{name}` was not built" if table is None
            else f"column `{column}` not in `{name}`" if column not in table.data
            else f"aggregation `{aggregation}` not supported (only {sorted(AGGREGATIONS)})" if aggregation not in AGGREGATIONS
            else ""
        )
        profile[iid], profile[f"{iid}_year"] = "", ""
        types[iid], types[f"{iid}_year"] = (table.types.get(column, "text") if table else "text"), "text"
        if problem:
            report.add("Errors", f"Profile indicator `{iid}`: {problem}")
            continue
        df = table.data
        if ind["filter"]:
            df = df.query(ind["filter"])
        picked = _latest(df, column, table.plan.output_name.period)
        dupes = picked[picked.duplicated("lgd_district_code", keep=False)]
        if len(dupes):
            report.add("Errors", f"Profile indicator `{iid}`: several rows per district at the latest time "
                       f"({dupes['lgd_district_code'].nunique()} districts); add a filter. Left empty for those districts.")
            picked = picked.drop_duplicates("lgd_district_code", keep=False)
        values = dict(zip(picked["lgd_district_code"], picked["value"]))
        years = dict(zip(picked["lgd_district_code"], picked["year"]))
        profile[iid] = profile["lgd_district_code"].map(values).fillna("")
        profile[f"{iid}_year"] = profile["lgd_district_code"].map(years).fillna("")
        missing = profile.loc[profile[iid] == "", "district"].tolist()
        year_set = sorted(set(years.values()))
        report.add("District profile", f"`{iid}`: {len(values)}/{len(profile)} districts; year(s) {', '.join(year_set)}"
                   + (f"; empty: {', '.join(missing)}" if missing else ""))

    profile = profile.reset_index(drop=True)
    write_csv(profile, state_dir / "district-profile.csv")
    write_json(profile, types, state_dir, "district-profile")
