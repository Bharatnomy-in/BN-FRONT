"""Decide which warehouse tables go into the front repo, their lens, and merge groups.

A "plan" is one output dataset: one or more warehouse parts (more than one when a
table was split by period) plus the output name and lens.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from .config import Config, Reference, State
from .naming import DatasetName, make_period, period_bounds
from .report import Report


@dataclass
class DatasetPlan:
    parts: list[str]  # warehouse folder names, oldest period first
    output_name: DatasetName
    lens_id: str


class LensError(RuntimeError):
    pass


def district_tables(warehouse: Path) -> list[str]:
    """Every warehouse folder whose LEVEL is DIST."""
    return sorted(
        p.name for p in warehouse.iterdir() if p.is_dir() and p.name.endswith("_DIST")
    )


def lens_for(dataset: str, cfg: Config, ref: Reference, report: Report) -> str | None:
    """Lens from variables.csv (most common); config/dataset_lens.csv wins on a tie or a gap."""
    counts = Counter(ref.variables.loc[ref.variables.dataset == dataset, "lens_id"])
    override = cfg.dataset_lens.get(dataset)
    if not counts:
        return override
    ranked = counts.most_common()
    split = ", ".join(f"{lens} {n}" for lens, n in ranked)
    tie = len(ranked) > 1 and ranked[0][1] == ranked[1][1]
    if tie:
        if override is None:
            raise LensError(f"{dataset}: variables.csv lenses are tied ({split}); add it to config/dataset_lens.csv")
        report.add("Lens assignment", f"`{dataset}`: tie in variables.csv ({split}); used `{override}` from config/dataset_lens.csv")
        return override
    if len(ranked) > 1:
        report.add("Lens assignment", f"`{dataset}`: variables span several lenses ({split}); used the most common, `{ranked[0][0]}`")
    return ranked[0][0]


def output_geography(name: DatasetName, state: State) -> str | None:
    """GEOGRAPHY for the output name, or None if the table cannot hold this state's rows."""
    if name.geography in ("STATES", state.code_short):
        return state.code_short
    return None  # another single state's table (e.g. KA_...), or IN


def plan_datasets(warehouse: Path, state: State, cfg: Config, ref: Reference, report: Report) -> list[DatasetPlan]:
    """Group district tables into output datasets and assign lenses."""
    groups: dict[tuple[str, ...], list[DatasetName]] = {}
    for folder in district_tables(warehouse):
        if folder in cfg.excluded:
            report.add("Datasets skipped", f"`{folder}`: {cfg.excluded[folder]}")
            continue
        name = DatasetName.parse(folder)
        geo = output_geography(name, state)
        if geo is None:
            report.add("Datasets skipped", f"`{folder}`: geography `{name.geography}` is not {state.code_short}")
            continue
        out = name.with_geography(geo)
        groups.setdefault(out.merge_key(), []).append(name)

    plans: list[DatasetPlan] = []
    missing_lens: list[str] = []
    for members in groups.values():
        members.sort(key=lambda n: period_bounds(n.period)[0])
        start = period_bounds(members[0].period)[0]
        end = period_bounds(members[-1].period)[1]
        out = members[-1].with_geography(state.code_short).with_period(make_period(start, end))
        parts = [str(m) for m in members]
        lenses = {p: lens_for(p, cfg, ref, report) for p in parts}
        known = {lens for lens in lenses.values() if lens}
        if not known:
            missing_lens += parts
            continue
        if len(known) > 1:
            raise LensError(f"Parts of {out} have different lenses: {lenses}")
        if len(parts) > 1:
            report.add("Merges", f"`{out}` ← " + " + ".join(f"`{p}`" for p in parts))
        plans.append(DatasetPlan(parts=parts, output_name=out, lens_id=known.pop()))

    if missing_lens:
        raise LensError(
            "No lens for these datasets. Add them to config/dataset_lens.csv "
            "(dataset,lens_id,note):\n  " + "\n  ".join(missing_lens)
        )
    return sorted(plans, key=lambda p: str(p.output_name))
