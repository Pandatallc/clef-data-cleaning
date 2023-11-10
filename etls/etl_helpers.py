
import numpy as np
import pandas as pd
from datetime import datetime
from typing import Sequence

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