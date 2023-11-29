import pandas as pd
from pathlib import Path

from etls.etl_helpers import try_strip


class VARuleReader:
    """Represents data in an excel sheet."""

    def __init__(self, sheet_name: str, head: int, tail: int, cols: str):
        self.sheet_name = sheet_name
        self.head = head
        self.tail = tail
        self.cols = cols
        self.rules = self._get_clean_rules()
        self.deltas = self.rules[
            self.rules["Value"] != self.rules["Rule (to be defined by CCF team)"]
        ]

    def _get_clean_rules(self):
        df = pd.read_excel(
            Path(
                "data", "raw", "ccf_apellis_data_cleaning_summary_20231120.xlsx"
            ),
            sheet_name=self.sheet_name,
            header=self.head,
            usecols=self.cols,
        ).iloc[: self.tail]

        df["Value"] = [try_strip(x) for x in df["Value"]]
        clean_rules = pd.DataFrame(df.groupby(["Value", "Rule (to be defined by CCF team)"])["Occurences"].sum()).reset_index()
        return clean_rules

    def delta_dict(self) -> dict:
        return {
            row["Value"]: row["Rule (to be defined by CCF team)"]
            for i, row in self.deltas.iterrows()
        }

    def occurances(self) -> dict:
        return sum(self.deltas["Occurances"])
    

def get_col_map(args) -> dict:
    """A mapping dict for making str and num replacements"""
    str_rules = VARuleReader(
                args["sheet_name"],
                args["str_head"],
                args["str_tail"],
                args["str_cols"],
            )
    try:
        num_rules = VARuleReader(
            args["sheet_name"],
            args["num_head"],
            args["num_tail"],
            args["num_cols"],
        )
        col_map = num_rules.delta_dict() | str_rules.delta_dict()
    except KeyError:
        col_map=str_rules.delta_dict()
    return col_map

def get_occs(args) -> pd.DataFrame:
    str_rules = VARuleReader(
                args["sheet_name"],
                args["str_head"],
                args["str_tail"],
                args["str_cols"],
            )
    try:
        num_rules = VARuleReader(
            args["sheet_name"],
            args["num_head"],
            args["num_tail"],
            args["num_cols"],
        )
        occ_df = pd.concat([num_rules.rules, str_rules.rules])
    except KeyError:
        occ_df=str_rules.rules
    return occ_df
