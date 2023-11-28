import numpy as np
import pandas as pd
from datetime import datetime
from typing import Mapping, Sequence


def try_str_to_date(val):
    try:
        return datetime.strptime(val, "%Y-%m-%d %H:%M:%S").date()
    except:
        return val


def try_str_to_float(val):
    try:
        return float(val)
    except:
        return val


def string_to_blank_save_numeric(col: Sequence) -> Sequence:
    """Converts all values of type str to NaN. Keeps numeric strings."""
    result = [np.nan if type(try_str_to_float(x)) == str else x for x in col]
    return pd.Series(result, name=col.name)


def string_to_blank_save_date(col: Sequence) -> Sequence:
    """Converts all values of type str to NaN. Keeps dates strings."""
    result = [np.nan if type(try_str_to_date(x)) == str else x for x in col]
    return pd.Series(result, name=col.name)


def date_to_blank(col: Sequence) -> Sequence:
    result = [np.nan if type(try_str_to_date(x)) == datetime.date else x for x in col]
    return result


def value_map(col: Sequence, val_map: Mapping) -> Sequence:
    mapped_seq = [val_map.get(x, x) for x in col]
    new_seq = [np.nan if x == "Replace with blank" else x for x in mapped_seq]
    return pd.Series(new_seq, name=col.name)
