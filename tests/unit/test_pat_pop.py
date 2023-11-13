import pytest
from etls.sheets.pat_pop import PatpopScrub
from etls.instructions import pat_pop as pat_pop_ins

from tests.conftest import *

class TestPatpopScrub:
    pat_pop_df = pd.read_csv("data/interim/pat_pop.csv")
    pat_pop_instructions = pat_pop_ins
    error_kv_list = [(k,v) for k,v in pat_pop_delta_counts.items()]

    def display_check(self, result):
        old_col = result[0]
        new_cols = result[1]
        diff = old_col.compare(new_cols[0], result_names=(old_col.name, new_cols[0].name))
        if len(new_cols)>1:
            idx = list(diff.index) 
            cols = [old_col]+new_cols
            return pd.DataFrame(cols).T.loc[idx]
        return diff

    @pytest.mark.parametrize("col_name,expected", [("OCT_DATE", mock_oct_date_notes),("Sub-RPE 5mm OD", mock_sub_rpe_od_notes)])
    def test__get_notes(self, col_name, expected):
        col = self.__class__.pat_pop_df[col_name]
        ins = self.__class__.pat_pop_instructions[col_name]
        assert list(PatpopScrub(col, ins).notes) == expected

    @pytest.mark.parametrize("col_name,expected", error_kv_list)
    def test_clean_delta_counts(self, col_name,expected):
        col = self.__class__.pat_pop_df[col_name]
        ins = self.__class__.pat_pop_instructions[col_name]
        diff = self.display_check(PatpopScrub(col,ins).clean())
        assert len(diff) == expected