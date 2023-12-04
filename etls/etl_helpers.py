import numpy as np
import pandas as pd
import datetime
from typing import Mapping, Sequence, Any


def try_str_to_date(val):
    try:
        return datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S").date()
    except:
        return val


def try_str_to_float(val):
    try:
        return float(val)
    except:
        return val


def try_strip(x):
    """strip white space around strings, and convert solely whitespace to np.nan"""
    try:
        res = x.strip()
    except:
        res = x
    return np.nan if res == "" else res


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
    return pd.Series(result, name=col.name)

def try_make_numeric(x):
    try:
        if "." in x:
            return float(x)
        return int(x)
    except:
        return x
    
def numeric_col(col: Sequence) -> Sequence:
    result = [try_make_numeric(x) for x in col]
    return pd.Series(result, name= col.name)

def value_map(col: Sequence, val_map: Mapping[str, Any]) -> Sequence:
    """Maps values in a sequence to keys in a dictionary.
    In our case, we can expect all keys in our dictionary to be strings."""
    date_zoot = date_to_blank(col)
    mapped_seq = [val_map.get(try_int_to_str(x), x) for x in date_zoot]
    new_seq = [
        np.nan if x in ["Change to blank", "Replace with blank"] else x
        for x in mapped_seq
    ]
    return pd.Series(new_seq, name=col.name)


def try_int_to_str(x):
    if np.isreal(x):
        return str(x)
    return x
