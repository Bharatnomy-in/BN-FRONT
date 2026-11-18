"""Parse and rewrite warehouse dataset names.

Scheme: CATEGORY_subject_PERIOD_GEOGRAPHY_SOURCE_LEVEL, e.g.
CLM_cyclone-crossings_1982-to-2025_STATES_BNY_DIST.
"""
from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class DatasetName:
    category: str
    subject: str
    period: str
    geography: str
    source: str
    level: str

    @classmethod
    def parse(cls, name: str) -> "DatasetName":
        parts = name.split("_")
        if len(parts) != 6:
            raise ValueError(f"Dataset name does not have 6 parts: {name}")
        return cls(*parts)

    def __str__(self) -> str:
        return "_".join(
            [self.category, self.subject, self.period, self.geography, self.source, self.level]
        )

    def merge_key(self) -> tuple[str, ...]:
        """Parts that must match for two tables to be merged (everything but PERIOD)."""
        return (self.category, self.subject, self.geography, self.source, self.level)

    def with_geography(self, geography: str) -> "DatasetName":
        return replace(self, geography=geography)

    def with_period(self, period: str) -> "DatasetName":
        return replace(self, period=period)


def period_bounds(period: str) -> tuple[str, str]:
    """'1997-98-to-2009-10' -> ('1997-98', '2009-10'); '2023' -> ('2023', '2023')."""
    if "-to-" in period:
        start, end = period.split("-to-", 1)
        return start, end
    return period, period


def make_period(start: str, end: str) -> str:
    return start if start == end else f"{start}-to-{end}"
