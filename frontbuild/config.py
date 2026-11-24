"""Load the hand-edited files in config/ and the warehouse's _reference/ tables.

Everything is read as text so codes like 466 never turn into 466.0.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "config"


def read_text_csv(path: Path, comment: str | None = None) -> pd.DataFrame:
    """Read a CSV with every cell as a string and empty cells as ''."""
    return pd.read_csv(path, dtype=str, keep_default_na=False, comment=comment)


@dataclass(frozen=True)
class State:
    slug: str  # folder name, e.g. "maharashtra"
    code_short: str  # GEOGRAPHY code used in file names, e.g. "MH"
    lgd_state_code: str  # e.g. "27"


@dataclass
class Config:
    states: list[State]
    lens_folders: dict[str, str]  # lens_id -> folder name
    dataset_lens: dict[str, str]  # warehouse dataset -> lens_id (overrides)
    included: dict[str, str]  # warehouse dataset -> why it is shipped (the curated list; nothing else is)
    derived: pd.DataFrame
    profile_indicators: pd.DataFrame


def load_config() -> Config:
    states = [
        State(r["state_slug"], r["state_code_short"], r["lgd_state_code"])
        for r in read_text_csv(CONFIG_DIR / "states.csv").to_dict("records")
    ]
    lens = read_text_csv(CONFIG_DIR / "lens_folders.csv")
    dataset_lens = read_text_csv(CONFIG_DIR / "dataset_lens.csv")
    included = read_text_csv(CONFIG_DIR / "included_datasets.csv")
    return Config(
        states=states,
        lens_folders=dict(zip(lens.lens_id, lens.folder)),
        dataset_lens=dict(zip(dataset_lens.dataset, dataset_lens.lens_id)),
        included=dict(zip(included.dataset, included.reason)),
        derived=read_text_csv(CONFIG_DIR / "derived_columns.csv", comment="#"),
        profile_indicators=read_text_csv(CONFIG_DIR / "profile_indicators.csv", comment="#"),
    )


@dataclass
class Reference:
    """The warehouse's _reference/ tables."""

    geography: pd.DataFrame
    variables: pd.DataFrame
    lenses: pd.DataFrame

    def districts(self, lgd_state_code: str) -> pd.DataFrame:
        """District rows of geography.csv for one state."""
        g = self.geography
        mask = (g["level"] == "district") & (g["lgd_state_code"] == lgd_state_code)
        return pd.DataFrame(g.loc[mask]).reset_index(drop=True)


def load_reference(warehouse: Path) -> Reference:
    ref = warehouse / "_reference"
    return Reference(
        geography=read_text_csv(ref / "geography.csv"),
        variables=read_text_csv(ref / "variables.csv"),
        lenses=read_text_csv(ref / "lenses.csv"),
    )
