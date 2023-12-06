import os
import pandas as pd
from pathlib import Path

from etls.etl_helpers import try_strip, try_int_to_str


class VARuleReader:
    """Represents Visual Accuity Rule reader, reads lookup table for rules.
    Important to remember this performs light cleaning for the consistency of lookups
     - strip whitespace
     - turn empty string col to nan
     - convert integers to strings
    """

    def __init__(self, sheet_name: str, head: int, tail: int, cols: str):
        self.sheet_name = sheet_name
        self.head: int = head
        self.tail: int = tail
        self.cols: str = cols
        self.rules: pd.DataFrame = self._get_clean_rules()
        self.deltas: pd.DataFrame = self.rules[
            self.rules["Value"] != self.rules["Rule (to be defined by CCF team)"]
        ]

    def _get_clean_rules(self):
        """Reads rules and strips whitespace from Values, converts numeric to string for easier look up"""
        fp = Path("data", "raw", "ccf_apellis_data_cleaning_summary_20231205.xlsx")
        if not os.path.exists(fp):
            fp = Path("..", fp)

        df = pd.read_excel(
            fp,
            sheet_name=self.sheet_name,
            header=self.head,
            usecols=self.cols,
        ).iloc[: self.tail]

        # remove all white space
        df["Value"] = [try_strip(x) for x in df["Value"]]
        # convert ints to str, for consistent mapping to column values
        df["Value"] = [try_int_to_str(x) for x in df["Value"]]
        # New total of occurences
        groupby_cols = ["Value", "Rule (to be defined by CCF team)"]
        if df.shape[1] == 4:
            groupby_cols = groupby_cols + ["Add'l notes"]
        try:
            clean_rules = pd.DataFrame(
                df.groupby(groupby_cols)["Occurences"].sum()
            ).reset_index()
        except KeyError:
            clean_rules= pd.DataFrame(
                df.groupby(groupby_cols)["Occurrences"].sum().reset_index()
            )
        return clean_rules

    def delta_dict(self) -> dict:
        return {
            row["Value"]: row["Rule (to be defined by CCF team)"]
            for i, row in self.deltas.iterrows()
        }

    def rules_dict(self) -> dict:
        return {
            row["Value"]: row["Rule (to be defined by CCF team)"]
            for i, row in self.rules.iterrows()
        }

    def occurances(self) -> dict:
        return sum(self.deltas["Occurances"])


def get_all_rules(args) -> pd.DataFrame:
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
        all_rules = pd.concat([str_rules.rules, num_rules.rules])
        clean_rules = pd.DataFrame(
            all_rules.groupby(["Value", "Rule (to be defined by CCF team)"])[
                "Occurences"
            ].sum()
        ).reset_index()
    except KeyError:
        clean_rules = str_rules.rules
    return clean_rules


def get_col_map_all(args) -> dict:
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
        col_map = num_rules.rules_dict() | str_rules.rules_dict()
    except KeyError:
        col_map = str_rules.rules_dict()
    return col_map
