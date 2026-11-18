"""Write tables as CSV and JSON (or JSON Lines), byte-for-byte deterministic.

JSON numbers are written from the original text when that text is already a valid
JSON number, so `12.50` stays `12.50` (no float rounding surprises).
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import pandas as pd

JSON_NUMBER_RE = re.compile(r"^-?(0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?$")
JSONL_THRESHOLD_BYTES = 25 * 1024 * 1024


def write_csv(df: pd.DataFrame, path: Path) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(df.columns)
        writer.writerows(df.itertuples(index=False, name=None))


def json_value(value: str, kind: str) -> str:
    """One cell as a JSON token. kind is text / integer / number."""
    if value == "":
        return "null"
    if kind == "text":
        return json.dumps(value, ensure_ascii=False)
    if JSON_NUMBER_RE.match(value):
        return value
    # e.g. '+5', '.5', '007': let Python normalise it.
    number = float(value)
    return str(int(number)) if kind == "integer" else json.dumps(number)


def json_rows(df: pd.DataFrame, types: dict[str, str]) -> list[str]:
    keys = [json.dumps(c, ensure_ascii=False) for c in df.columns]
    kinds = [types.get(c, "text") for c in df.columns]
    rows = []
    for record in df.itertuples(index=False, name=None):
        cells = ",".join(f"{k}:{json_value(v, t)}" for k, v, t in zip(keys, record, kinds))
        rows.append("{" + cells + "}")
    return rows


def write_json(df: pd.DataFrame, types: dict[str, str], folder: Path, name: str) -> str:
    """Write <name>.json, or <name>.jsonl if the JSON would be over ~25 MB. Returns the file name."""
    rows = json_rows(df, types)
    text = "[" + ",".join(rows) + "]\n"
    if len(text.encode("utf-8")) <= JSONL_THRESHOLD_BYTES:
        filename = f"{name}.json"
    else:
        filename = f"{name}.jsonl"
        text = "\n".join(rows) + "\n"
    (folder / filename).write_text(text, encoding="utf-8")
    return filename
