"""Run the whole build for every state in config/states.csv.

Everything under states/<slug>/ is deleted and written again on each build, so
nothing stale is left behind and output only depends on the warehouse commit + config.
"""
from __future__ import annotations

import json
import shutil
from datetime import date
from pathlib import Path

from .config import ROOT, Config, Reference, State, load_config, load_reference
from .boundaries import build_geojson
from .discover import plan_datasets
from .docs import attribution, state_readme
from .profile import build_profile
from .readme import WarehouseReadme, dataset_readme, lens_readme, parse_readme
from .report import Report
from .tables import CleanTable, build_table
from .writers import write_csv, write_json

STATES_DIR = ROOT / "states"
BUILD_INFO = ROOT / "BUILD_INFO.json"
BUILD_REPORT = ROOT / "BUILD_REPORT.md"


def state_display_name(state: State, ref: Reference) -> str:
    g = ref.geography
    rows = g[(g["level"] == "state") & (g["lgd_state_code"] == state.lgd_state_code)]
    return rows["state_ut"].iloc[0] if len(rows) else state.slug.title()


def build_state(state: State, cfg: Config, ref: Reference, warehouse: Path, sha: str, report: Report) -> list[dict]:
    """Write all dataset folders and lens READMEs for one state. Returns BUILD_INFO entries."""
    state_dir = STATES_DIR / state.slug
    if state_dir.exists():
        shutil.rmtree(state_dir)
    state_name = state_display_name(state, ref)
    all_districts = ref.districts(state.lgd_state_code)
    lens_names = dict(zip(ref.lenses["lens_id"], ref.lenses["lens_name"]))
    lens_rows: dict[str, list[tuple[str, str, str, int]]] = {lens: [] for lens in cfg.lens_folders}
    info: list[dict] = []
    tables: dict[str, CleanTable] = {}  # output name -> table, for the district profile

    for plan in plan_datasets(warehouse, state, cfg, ref, report):
        table = build_table(warehouse, plan, state, ref, cfg.derived, report)
        name = str(plan.output_name)
        if table.data.empty:
            report.add("Datasets skipped", f"`{name}`: no {state.code_short} rows after filtering")
            continue
        folder = state_dir / cfg.lens_folders[plan.lens_id] / name
        folder.mkdir(parents=True)
        write_csv(table.data, folder / f"{name}.csv")
        json_file = write_json(table.data, table.types, folder, name)
        docs = [parse_readme(warehouse / p / "README.md", p, sha) for p in plan.parts]
        text, undocumented = dataset_readme(table, docs, state_name, len(all_districts), json_file, sha)
        (folder / "README.md").write_text(text, encoding="utf-8")
        if undocumented:
            report.add("Cleaning", f"`{name}`: no description in the warehouse README for {len(undocumented)} column(s): {undocumented}")

        missing = sorted(set(all_districts["district"]) - set(table.data["district"]))
        if missing:
            report.add("Districts missing per dataset", f"`{name}`: {len(missing)} missing ({', '.join(missing)})")
        report.add("Datasets included", f"`{name}` → `{cfg.lens_folders[plan.lens_id]}/` ({len(table.data):,} rows)")
        tables[name] = table
        lens_rows[plan.lens_id].append((name, docs[-1].title, plan.output_name.period, len(table.data)))
        info.append(_info_entry(table, state, cfg, json_file))

    for lens_id, folder_name in cfg.lens_folders.items():
        lens_dir = state_dir / folder_name
        lens_dir.mkdir(parents=True, exist_ok=True)
        text = lens_readme(lens_names.get(lens_id, lens_id), state_name, lens_rows[lens_id])
        (lens_dir / "README.md").write_text(text, encoding="utf-8")
    build_geojson(warehouse, state, ref, state_dir / "districts.geojson", report)
    build_profile(tables, state, ref, cfg.profile_indicators, state_dir, report)

    new_districts = all_districts[all_districts["created_after_2011"] == "yes"]
    boundary_notes = [f"**{r['district']}** (`{r['lgd_district_code']}`) was created after 2011 and has no boundary yet "
                      "(`geometry: null`); its area is inside its parent district's 2011 polygon."
                      for r in new_districts.to_dict("records")]
    text = state_readme(state, state_name, cfg, info, warehouse, sha, lens_names, cfg.profile_indicators, boundary_notes)
    (state_dir / "README.md").write_text(text, encoding="utf-8")
    return info


def _info_entry(table: CleanTable, state: State, cfg: Config, json_file: str) -> dict:
    name = str(table.plan.output_name)
    return {
        "state": state.slug,
        "dataset": name,
        "lens": table.plan.lens_id,
        "path": f"states/{state.slug}/{cfg.lens_folders[table.plan.lens_id]}/{name}",
        "json_file": json_file,
        "warehouse_parts": table.plan.parts,
        "rows": len(table.data),
        # Row accounting the checks use: warehouse rows - totals dropped - merge drops = rows.
        "warehouse_rows_for_state": table.warehouse_rows,
        "state_total_rows_dropped": table.state_total_rows_dropped,
        "merge_duplicates_dropped": table.merge_duplicates_dropped,
        "merge_conflicts_dropped": table.merge_conflicts_dropped,
        "columns": list(table.data.columns),
    }


def compare_columns(old_info: dict | None, datasets: list[dict], report: Report) -> None:
    if not old_info:
        report.add("Column changes since last build", "No previous build to compare with.")
        return
    old = {d["dataset"]: d for d in old_info.get("datasets", [])}
    for d in datasets:
        before = old.get(d["dataset"])
        if before is None:
            report.add("Column changes since last build", f"`{d['dataset']}`: new dataset")
            continue
        added = [c for c in d["columns"] if c not in before["columns"]]
        removed = [c for c in before["columns"] if c not in d["columns"]]
        if added or removed:
            report.add("Column changes since last build", f"`{d['dataset']}`: added {added}, removed {removed}")
    for name in sorted(set(old) - {d["dataset"] for d in datasets}):
        report.add("Column changes since last build", f"`{name}`: dataset no longer built")


def run_build(warehouse: Path, sha: str) -> Report:
    cfg = load_config()
    ref = load_reference(warehouse)
    report = Report(sha)
    old_info = json.loads(BUILD_INFO.read_text()) if BUILD_INFO.exists() else None
    datasets: list[dict] = []
    for state in cfg.states:
        datasets += build_state(state, cfg, ref, warehouse, sha, report)
    compare_columns(old_info, datasets, report)
    info = {
        "warehouse_repo": "https://github.com/sarveshkant2003-afk/bharatnomy-data",
        "warehouse_sha": sha,
        "build_date": date.today().isoformat(),
        "datasets": datasets,
    }
    (ROOT / "ATTRIBUTION.md").write_text(attribution(datasets, warehouse, sha), encoding="utf-8")
    BUILD_INFO.write_text(json.dumps(info, indent=2, ensure_ascii=False) + "\n")
    report.write(BUILD_REPORT)
    return report
