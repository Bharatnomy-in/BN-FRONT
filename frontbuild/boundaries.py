"""Write states/<slug>/districts.geojson from the Census 2011 DataMeet district map.

Polygons are matched to today's districts by Census 2011 district code (never by name),
using `census2011_district_code` in geography.csv. Districts created after 2011 have no
2011 polygon; they are kept as features with `geometry: null` and a `boundary_note`.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import geopandas as gpd
import shapely

from .config import Reference, State
from .report import Report

SHAPEFILE = "_sources/datameet-maps/raw/datameet-maps_census2011-districts_2011.shp"
SIMPLIFY_TOLERANCE_DEG = 0.001  # about 100 m; shared borders stay shared (coverage simplify)
DECIMALS = 5
MAX_BYTES = 3 * 1024 * 1024


def _round_coords(obj):
    """Round every coordinate in a GeoJSON geometry dict to DECIMALS places."""
    if isinstance(obj, (list, tuple)):
        if obj and isinstance(obj[0], float):
            return [round(v, DECIMALS) for v in obj]
        return [_round_coords(o) for o in obj]
    return obj


def _parent_notes(districts) -> dict[str, str]:
    """2011 code of a parent district -> note naming the newer district(s) carved out of it."""
    notes: dict[str, list[str]] = {}
    for row in districts[districts["created_after_2011"] == "yes"].to_dict("records"):
        for code in re.findall(r"Census 2011 district (\d+)", row["note"]):
            notes.setdefault(str(int(code)), []).append(row["district"])
    return {code: f"2011 boundary; includes present-day {', '.join(names)}" for code, names in notes.items()}


def build_geojson(warehouse: Path, state: State, ref: Reference, out_path: Path, report: Report) -> None:
    districts = ref.districts(state.lgd_state_code)
    shapes = gpd.read_file(warehouse / SHAPEFILE).to_crs(epsg=4326)
    shapes["code"] = shapes["censuscode"].astype(int).astype(str)
    wanted = {str(int(c)) for c in districts["census2011_district_code"] if c}
    shapes = shapes[shapes["code"].isin(sorted(wanted))].sort_values("code").reset_index(drop=True)

    # Fix any invalid ring, then simplify all polygons together so neighbours keep one shared edge.
    geoms = shapely.make_valid(shapes.geometry.values)
    geoms = shapely.coverage_simplify(geoms, SIMPLIFY_TOLERANCE_DEG)
    geoms = shapely.set_precision(geoms, 10 ** -DECIMALS)  # snap to the 5-decimal grid, stays valid
    by_code = dict(zip(shapes["code"], geoms))
    parent_notes = _parent_notes(districts)

    features = []
    rows = sorted(districts.to_dict("records"), key=lambda r: int(r["lgd_district_code"]))
    for row in rows:
        code2011 = str(int(row["census2011_district_code"])) if row["census2011_district_code"] else ""
        props = {
            "lgd_district_code": row["lgd_district_code"],
            "district": row["district"],
            "lgd_state_code": row["lgd_state_code"],
            "state_ut": row["state_ut"],
            "census2011_district_code": row["census2011_district_code"] or None,
        }
        geom = by_code.get(code2011)
        if geom is None:
            note = "No 2011 boundary: district created after 2011. " + row["note"]
            props["boundary_note"] = note.strip()
            report.add("Boundaries", f"{state.slug}: **{row['district']}** ({row['lgd_district_code']}) has no 2011 polygon; geometry is null. {row['note']}")
            geometry = None
        else:
            if code2011 in parent_notes:
                props["boundary_note"] = parent_notes[code2011]
            if not shapely.is_valid(geom):
                report.add("Errors", f"{state.slug}: invalid geometry for {row['district']}")
            geometry = json.loads(json.dumps(shapely.geometry.mapping(geom)))  # tuples -> lists
            geometry["coordinates"] = _round_coords(geometry["coordinates"])
        features.append({"type": "Feature", "properties": props, "geometry": geometry})

    unmatched = wanted - {str(int(r["census2011_district_code"])) for r in rows if r["census2011_district_code"]}
    if unmatched:
        report.add("Errors", f"{state.slug}: 2011 polygons not matched to a district: {sorted(unmatched)}")
    text = json.dumps({"type": "FeatureCollection", "features": features}, ensure_ascii=False, separators=(",", ":")) + "\n"
    out_path.write_text(text, encoding="utf-8")
    size = len(text.encode("utf-8"))
    report.add("Boundaries", f"{state.slug}: {len(features)} features, {size / 1e6:.2f} MB (simplified at {SIMPLIFY_TOLERANCE_DEG}°, {DECIMALS} decimals)")
    if size > MAX_BYTES:
        report.add("Errors", f"{out_path.name} is {size / 1e6:.1f} MB; raise SIMPLIFY_TOLERANCE_DEG")
