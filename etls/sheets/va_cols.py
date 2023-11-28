import pandas as pd
from pathlib import Path


class VARuleReader:
    """Represents data in an excel sheet."""

    def __init__(self, sheet_name: str, head: int, tail: int, cols: str):
        self.sheet_name = sheet_name
        self.head = head
        self.tail = tail
        self.cols = cols
        self.rules = pd.read_excel(
            Path(
                "data", "raw", "ccf_apellis_data_cleaning_summary_20231120.xlsx"
            ),
            sheet_name=self.sheet_name,
            header=self.head,
            usecols=self.cols,
        ).iloc[: self.tail]
        self.deltas = self.rules[
            self.rules["Value"] != self.rules["Rule (to be defined by CCF team)"]
        ]

    def delta_dict(self) -> dict:
        return {
            row["Value"]: row["Rule (to be defined by CCF team)"]
            for i, row in self.deltas.iterrows()
        }

    def occurances(self) -> dict:
        return sum(self.deltas["Occurances"])
