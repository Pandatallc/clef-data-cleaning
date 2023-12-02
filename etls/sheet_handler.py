import pandas as pd
import os
from typing import Tuple

from etls.sheets.scrubbers import BasicScrubber, FancyScrubber
from .etl_helpers import *


class SheetHandler:
    """An object that represents the Sheet and the process parameters for its cleaning. [patpop, ophthafterdxdate, dxaferdxdate, others]"""

    def __init__(self, sheet_name: Tuple, instructions: dict):
        """sheet_name will determine the Scrubbing logic to follow,
        the instructions will indicate the parameters for the scrubbing."""
        self.clef_sheet_name = sheet_name[0]
        self.deliv_sheet_name = sheet_name[1]
        self.instructions = instructions.get(self.clef_sheet_name, {})
        self.raw = self._get_raw()
        self.column_names = self.raw.columns

    def _get_raw(self):
        try:
            return pd.read_csv(f"data/interim/{self.sheet_name}.csv", low_memory=False)
        except FileNotFoundError:
            raw = pd.read_excel(
                "../data/raw/MASTER FILE.xlsx",
                sheet_name=self.deliv_sheet_name,
                index_col=0,
                header=0,
            )
            raw.dropna(how="all", axis=1, inplace=True)
            raw.reset_index(inplace=True)
            raw.to_csv(f"../data/interim/{self.sheet_name}.csv", index=False)
            return raw

    def clean_col(self, col_name):
        if col_name not in self.column_names:
            raise KeyError(
                f"Column '{col_name}' does not exist in sheet '{self.sheet_name}'."
            )
        if self.clef_sheet_name in ["pat_pop", "ophthafterdxdate"]:
            scrub_res = FancyScrubber(
                self.raw[col_name], self.instructions[col_name]
            ).clean()
        else:
            scrub_res = BasicScrubber(self.raw[col_name]).clean()
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
