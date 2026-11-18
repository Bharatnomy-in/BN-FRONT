"""Small unit tests for the pure helper functions."""
import pandas as pd

from frontbuild.naming import DatasetName, make_period, period_bounds
from frontbuild.tables import _short_financial_year, infer_types, sort_rows
from frontbuild.writers import json_value


def test_name_round_trip_and_geography():
    name = DatasetName.parse("CLM_cyclone-crossings_1982-to-2025_STATES_BNY_DIST")
    assert str(name.with_geography("MH")) == "CLM_cyclone-crossings_1982-to-2025_MH_BNY_DIST"


def test_period_helpers():
    assert period_bounds("1997-98-to-2009-10") == ("1997-98", "2009-10")
    assert period_bounds("2023") == ("2023", "2023")
    assert make_period("1997-98", "2022-23") == "1997-98-to-2022-23"


def test_codes_stay_text_and_numbers_are_typed():
    df = pd.DataFrame({"lgd_district_code": ["466"], "year": ["2020"], "n": ["5"], "x": ["1.50"], "t": ["a"]})
    assert infer_types(df) == {"lgd_district_code": "text", "year": "text", "n": "integer", "x": "number", "t": "text"}


def test_json_value_keeps_number_text():
    assert json_value("1.50", "number") == "1.50"
    assert json_value("466", "text") == '"466"'
    assert json_value("", "number") == "null"
    assert json_value(".5", "number") == "0.5"


def test_financial_year():
    assert _short_financial_year("2010-2011") == "2010-11"
    assert _short_financial_year("2019-2021") == "2019-2021"


def test_sort_is_natural():
    df = pd.DataFrame({"lgd_district_code": ["467", "466", "466"], "age": ["10", "2", "All ages"]})
    out = sort_rows(df, {"lgd_district_code": "text", "age": "text"})
    assert list(out["age"]) == ["2", "All ages", "10"]
