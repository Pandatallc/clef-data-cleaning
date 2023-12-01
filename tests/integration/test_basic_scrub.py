import pytest
from etls.sheets.pat_pop import BasicScrubber
from etls.instructions import instructions

from tests.conftest import *


class TestBasicScrub:
    def display_check(self, result):
        old_col = result[0]
        new_cols = result[1]
        diff = old_col.compare(
            new_cols[0], result_names=(old_col.name, new_cols[0].name)
        )
        if len(new_cols) > 1:
            idx = list(diff.index)
            cols = [old_col] + new_cols
            return pd.DataFrame(cols).T.loc[idx]
        return diff

    def test_clean_delta_counts(self, mock_dxafterdxdate):
        col_name = "CURRENT_ICD9_LIST"
        col = mock_dxafterdxdate[col_name]
        diff = self.display_check(BasicScrubber(col).clean())
        assert len(diff) == 40479
