import pandas as pd
import os

from etls.sheets.pat_pop import PatpopScrub
from .etl_helpers import *

pat_pop_csv ="data/interim/pat_pop.csv"



class SheetCleaner:
    """Returns a pd.DataFrame with all instructions"""
    def __init__(self, sheet_name: str, instructions: dict):
        self.sheet_name = sheet_name
        self.instructions = instructions
        self.raw = pd.read_csv(pat_pop_csv)

    def get_clean(self):
        """Assembles clean data one sheet at a time"""
        col_list = [] 
        for col in self.raw.columns: #List[Str]
            if col in self.instructions:
                scrub_res = PatpopScrub(self.raw[col], self.instructions[col]).clean()
                col_list += scrub_res[1]
            else:
                col_list.append(self.raw[col])
        return pd.DataFrame(col_list).T



