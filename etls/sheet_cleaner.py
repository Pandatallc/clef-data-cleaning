import pandas as pd
import os

from etls.sheets.pat_pop import DxAfterDxdateScrub, PatpopScrub
from .etl_helpers import *


class SheetCleaner:
    """An object that represents the Sheet and the process parameters for its cleaning. [patpop, ophthafterdxdate, dxaferdxdate, others]"""

    def __init__(self, sheet_name: str, instructions: dict):
        """sheet_name will determine the Scrubbing logic to follow,
        the instructions will indicate the parameters for the scrubbing."""
        self.sheet_name = sheet_name
        self.instructions = instructions.get(sheet_name, None)
        self.raw = pd.read_csv(f"data/interim/{sheet_name}.csv")
        self.column_names = self.raw.columns

    def clean_col(self, col_name):
        if col_name not in self.column_names:
            raise KeyError(
                f"Column '{col_name}' does not exist in sheet '{self.sheen_name}'."
            )
        if self.sheet_name in ["pat_pop", "ophthafterdxdate"]:
            scrub_res = PatpopScrub(self.raw[col_name], self.instructions[col_name]).clean()
        else:
            scrub_res = DxAfterDxdateScrub(self.raw[col_name]).clean()
        return scrub_res

    def get_clean_sheet(self):
        """Exports a clean dataset, all columns"""
        col_list = []
        for col in self.column_names:  # List[Str]
            if col in self.instructions:
                scrub_res = self.clean_col(col)
                col_list += scrub_res[1]
            else:
                col_list.append(self.raw[col])
        return pd.DataFrame(col_list).T
