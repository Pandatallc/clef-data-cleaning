from typing import Mapping, Sequence, Tuple
import numpy as np
import pandas as pd

from typing import List
from etls.etl_helpers import (
    date_to_blank,
    string_to_blank_save_date,
    string_to_blank_save_numeric,
    try_str_to_date,
    try_str_to_float,
    try_strip,
    value_map,
)
from etls.sheets.va_cols import VARuleReader, get_col_map_all


class PatpopScrub:
    """Logic for cleaning PatPop, and opthafterdxdate"""

    def __init__(self, col: Sequence, instructions: Mapping):
        self.format = instructions.get("format")
        self.string_intention = instructions["string_intention"]
        self.vals_to_notes = instructions.get("vals_to_notes", None)
        self.args = instructions.get("args", None)
        self.col_name = col.name
        self.old_col = pd.Series([try_strip(x) for x in col], name = f"old_{col.name}")
        self.notes_col_name = (
            f"{col.name}_notes" if instructions["string_intention"] != "blank" else None
        )
        self.notes = self._get_notes()

    def _get_notes(self):
        """If there are notes, we want to create them before turning them to null, so this is part of the initialization."""
        if self.string_intention not in ["blank", "map"]:
            if self.format == "date":
                return pd.Series(
                    [x if x in self.vals_to_notes else np.nan for x in self.old_col],
                    name=self.notes_col_name,
                )
            elif self.format == "numeric":
                return pd.Series(
                    [
                        x if type(try_str_to_float(x)) == str else np.nan
                        for x in self.old_col
                    ],
                    name=self.notes_col_name,
                )
            else:
                raise (
                    KeyError(
                        f"Cannot have string_intention 'notes' with format {self.format}"
                    )
                )
        if self.string_intention in ["blank", "map"]:
            return None

    def clean(self) -> Tuple[Sequence, List[Sequence]]:
        """Returns (old_column, [amended_column, optional(notes_column)])"""
        if self.format == "numeric":
            ammended_col = string_to_blank_save_numeric(self.old_col)
        if self.format == "date":
            ammended_col = string_to_blank_save_date(self.old_col)
        if self.string_intention == "map":
            col_map = get_col_map_all(args = self.args)
            mapped_col = value_map(
                self.old_col, col_map
            )
            ammended_col = pd.Series(date_to_blank(mapped_col), name=self.col_name)

        ## Add notes column
        if self.notes is not None:
            return (self.old_col, [ammended_col, self.notes])
        else:
            return (self.old_col, [ammended_col])


class DxAfterDxdateScrub:
    """Logic for cleaning DxAfterDxdate"""

    def __init__(self, col: Sequence):
        self.old_col = col.copy()
        self.col_name = self.old_col.name

    def clean(self) -> Tuple[Sequence, List[Sequence]]:
        """Returns (old_column, [amended_column, optional(notes_column)])"""
        ammended_cols_df = self.old_col.str.split(", ", expand=True)
        ammended_cols = []
        for i in ammended_cols_df.columns:
            ammended_col = ammended_cols_df[i].copy()
            ammended_col.name = f"{self.col_name}_{i+1}"
            ammended_cols.append(ammended_col)
        return (self.old_col, ammended_cols)


# class OpthafterDxDateScrub:
#     """Logic for cleaning OpthafterDxDate"""

#     def __init__(self, col: Sequence, instructions: Mapping):
#         self.format = instructions["format"]
#         self.string_intention = instructions["string_intention"]
#         self.vals_to_notes = instructions.get("vals_to_notes", None)
#         self.old_col = col.copy()
#         self.notes_col_name = (
#             f"{col.name}_notes" if instructions["string_intention"] != "blank" else None
#         )
#         self.old_col_name = f"old_{col.name}"
#         self.notes = self._get_notes()

#     def _get_notes(self):
#         """If there are notes, we want to create them before turning them to null, so this is part of the initialization."""
#         if self.string_intention != "blank":
#             if self.format == "date":
#                 return pd.Series(
#                     [x if x in self.vals_to_notes else np.nan for x in self.old_col],
#                     name=self.notes_col_name,
#                 )
#             elif self.format == "numeric":
#                 return pd.Series(
#                     [
#                         x if type(try_str_to_float(x)) == str else np.nan
#                         for x in self.old_col
#                     ],
#                     name=self.notes_col_name,
#                 )
#             else:
#                 raise (
#                     ValueError(
#                         f"Cannot have string_intention 'notes' with format {self.format}"
#                     )
#                 )
#         if self.string_intention == "blank":
#             return None

#     def clean(self) -> Tuple[Sequence, List[Sequence]]:
#         if
