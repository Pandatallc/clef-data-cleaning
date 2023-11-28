import pandas as pd
import os

from etls.sheets.pat_pop import DxAfterDxdateScrub, PatpopScrub
from .etl_helpers import *


class SheetCleaner:
    """Returns a pd.DataFrame with all instructions"""

    def __init__(self, sheet_name: str, instructions: dict):
        self.sheet_name = sheet_name
        self.instructions = instructions.get(sheet_name, None)
        self.raw = pd.read_csv(f"data/interim/{sheet_name}.csv")

    def get_clean(self):
        """Assembles clean data one sheet at a time"""
        col_list = []
        for col in self.raw.columns:  # List[Str]
            if col in self.instructions:
                if self.sheet_name == "pat_pop":
                    scrub_res = PatpopScrub(
                        self.raw[col], self.instructions[col]
                    ).clean()
                elif self.sheet_name == "dxafterdxdate":
                    scrub_res = DxAfterDxdateScrub(self.raw[col]).clean()
                elif self.sheet_name == "ophthafterdxdate":
                    scrub_res = PatpopScrub(
                        self.raw[col], self.instructions[col]
                    ).clean()
                col_list += scrub_res[1]
            else:
                col_list.append(self.raw[col])
        return pd.DataFrame(col_list).T
