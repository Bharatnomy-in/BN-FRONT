"""Checks on the built output (python build.py --check, pytest, and CI).

Returns (problems, warnings). Any problem fails the check.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import shapely
import shapely.geometry

from .config import ROOT, load_config, load_reference, read_text_csv

STATES_DIR = ROOT / "states"
WARN_BYTES = 50 * 1024 * 1024
FAIL_BYTES = 95 * 1024 * 1024


def run_checks(warehouse: Path) -> tuple[list[str], list[str]]:
    cfg = load_config()
    ref = load_reference(warehouse)
    info = json.loads((ROOT / "BUILD_INFO.json").read_text())
    problems: list[str] = []
    warnings: list[str] = []

    for state in cfg.states:
        state_dir = STATES_DIR / state.slug
        codes = set(ref.districts(state.lgd_state_code)["lgd_district_code"])
        for folder in cfg.lens_folders.values():
            if not (state_dir / folder / "README.md").exists():
                problems.append(f"{state.slug}/{folder}: lens folder has no README.md")
        entries = [d for d in info["datasets"] if d["state"] == state.slug]
        built = {d["path"] for d in entries}
        on_disk = {str(p.relative_to(ROOT)) for p in state_dir.glob("*/*") if p.is_dir()}
        for extra in sorted(on_disk - built):
            problems.append(f"{extra}: folder not in BUILD_INFO.json (stale output?)")
        for entry in entries:
            problems += check_dataset(ROOT / entry["path"], entry, state.lgd_state_code, codes, warehouse)
        if not (state_dir / "README.md").exists():
            problems.append(f"{state.slug}: state README.md missing")
        problems += check_profile(state_dir, len(codes), warnings)
        problems += check_geojson(state_dir, len(codes), warnings)

    for path in sorted(STATES_DIR.rglob("*")):
        if path.is_file():
            size = path.stat().st_size
            if size > FAIL_BYTES:
                problems.append(f"{path.relative_to(ROOT)}: {size / 1e6:.0f} MB is over 95 MB")
            elif size > WARN_BYTES:
                warnings.append(f"{path.relative_to(ROOT)}: {size / 1e6:.0f} MB is over 50 MB")
    return problems, warnings


def check_dataset(folder: Path, entry: dict, state_code: str, codes: set[str], warehouse: Path) -> list[str]:
    name = entry["dataset"]
    csv_path, json_path, readme = folder / f"{name}.csv", folder / entry["json_file"], folder / "README.md"
    missing = [p.name for p in (csv_path, json_path, readme) if not p.exists()]
    if missing:
        return [f"{name}: missing {missing}"]
    out: list[str] = []
    df = read_text_csv(csv_path)

    bad_state = df[df["lgd_state_code"] != state_code]
    if len(bad_state):
        out.append(f"{name}: {len(bad_state)} rows with another lgd_state_code")
    unknown = sorted(set(df["lgd_district_code"]) - codes)
    if unknown:
        out.append(f"{name}: lgd_district_code not in geography.csv for this state: {unknown}")

    # Row accounting, recounted straight from the warehouse files.
    wh_rows = 0
    for part in entry["warehouse_parts"]:
        raw = read_text_csv(warehouse / part / f"{part}.csv")
        wh_rows += int((raw["lgd_state_code"].str.strip() == state_code).sum())
    expected = wh_rows - entry["state_total_rows_dropped"] - entry["merge_duplicates_dropped"] - entry["merge_conflicts_dropped"]
    if len(df) != expected:
        out.append(f"{name}: {len(df)} rows, expected {expected} (warehouse {wh_rows} minus reported drops)")

    out += compare_csv_json(df, json_path, name)
    return out


def compare_csv_json(df, json_path: Path, name: str) -> list[str]:
    text = json_path.read_text(encoding="utf-8")
    rows = [json.loads(line) for line in text.splitlines()] if json_path.suffix == ".jsonl" else json.loads(text)
    if len(rows) != len(df):
        return [f"{name}: CSV has {len(df)} rows, JSON has {len(rows)}"]
    if rows and list(rows[0].keys()) != list(df.columns):
        return [f"{name}: CSV and JSON columns differ"]
    for i, (row, record) in enumerate(zip(df.itertuples(index=False, name=None), rows)):
        for col, csv_value, json_value in zip(df.columns, row, record.values()):
            if not _same(csv_value, json_value):
                return [f"{name}: row {i} column {col}: CSV {csv_value!r} vs JSON {json_value!r}"]
    return []


def _same(csv_value: str, json_value) -> bool:
    if json_value is None:
        return csv_value == ""
    if isinstance(json_value, str):
        return csv_value == json_value
    return float(csv_value) == float(json_value)


def check_profile(state_dir: Path, n_districts: int, warnings: list[str]) -> list[str]:
    path = state_dir / "district-profile.csv"
    if not path.exists():
        return [f"{path.relative_to(ROOT)}: missing"]
    with path.open(encoding="utf-8") as f:
        n = sum(1 for _ in csv.DictReader(f))
    return [] if n == n_districts else [f"{path.name}: {n} rows, expected {n_districts}"]


def check_geojson(state_dir: Path, n_districts: int, warnings: list[str]) -> list[str]:
    path = state_dir / "districts.geojson"
    if not path.exists():
        return [f"{path.relative_to(ROOT)}: missing"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"{path.name}: does not parse ({e})"]
    features = data.get("features", [])
    out = [] if len(features) == n_districts else [f"{path.name}: {len(features)} features, expected {n_districts}"]
    for f in features:
        geom = f.get("geometry")
        if geom is None:
            if not f["properties"].get("boundary_note"):
                out.append(f"{path.name}: {f['properties'].get('district')} has no geometry and no boundary_note")
        elif not shapely.is_valid(shapely.geometry.shape(geom)):
            out.append(f"{path.name}: invalid geometry for {f['properties'].get('district')}")
    return out
