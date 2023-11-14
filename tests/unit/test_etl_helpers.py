from datetime import date
from numpy import NaN
import pandas as pd
import pytest

from etls.etl_helpers import *


@pytest.mark.parametrize("val,expected", [("2019-08-28 00:00:00", date(2019, 8, 28))])
def test_try_str_to_date(val, expected):
    """Can't test NaN values here, use series operations (below)"""
    assert try_str_to_date(val) == expected


@pytest.mark.parametrize("val,expected", [("4.8", 4.8), ("'5", "'5")])
def test_try_str_to_float(val, expected):
    assert try_str_to_float(val) == expected


def test_string_to_blank_save_numeric():
    val = pd.Series(["hi", "", "4.6", 4.6])
    assert len(string_to_blank_save_numeric(val).compare(pd.Series([NaN, NaN, "4.6", 4.6]))) == 0

def test_string_to_blank_save_date():
    val = pd.Series(["2019-08-28 00:00:00", "", "4.6", 4.6])
    assert len(string_to_blank_save_date(val).compare(pd.Series(["2019-08-28 00:00:00", NaN, NaN, 4.6]))) == 0

