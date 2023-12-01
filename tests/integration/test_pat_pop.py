import pytest
from etls.sheets.pat_pop import PatpopScrub
from etls.instructions import instructions

from tests.conftest import *


class TestPatpopScrub:
    pat_pop_instructions = instructions["pat_pop"]
    ophthafterdxdate_instructions = instructions["ophthafterdxdate"]
    pat_pop_error_kv_list = [(k, v) for k, v in pat_pop_delta_counts.items()]
    oad_error_kv_list_normal = [
        (k, v) for k, v in opthafterdxdate_delta_counts.items() if "VA" not in k
    ]
    oad_error_kv_list_va = [
        (k, v) for k, v in opthafterdxdate_delta_counts.items() if "VA" in k
    ]

    # def mod_expected(self, df, col_name, rules, expected):
    #     rules_merge = pd.merge(rules, df[[col_name]], left_on=["Value"], right_on=[col_name], how="left")
    #     rules_merge["actual_occurences"] = rules_merge.groupby(col_name)[col_name].transform("size")
    #     mis_match = rules_merge[rules_merge["Occurences"] != rules_merge["actual_occurences"]]
    #     dups_dropped = mis_match.drop_duplicates(subset=["Value"])
    #     nan_count = sum(dups_dropped[dups_dropped["Value"].isnull()]["Occurences"])
    #     occ_diff = dups_dropped[~dups_dropped["Value"].isnull() & ~dups_dropped['actual_occurences'].isnull()]
    #     act_minus_exp = sum(occ_diff["actual_occurences"]) - sum(occ_diff["Occurences"])

    #     return expected + act_minus_exp - nan_count

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

    @pytest.mark.parametrize(
        "col_name,expected",
        [("OCT_DATE", mock_oct_date_notes), ("Sub-RPE 5mm OD", mock_sub_rpe_od_notes)],
    )
    def test__get_notes(self, col_name, expected, mock_pat_pop):
        col = mock_pat_pop[col_name]
        ins = self.__class__.pat_pop_instructions[col_name]
        assert list(PatpopScrub(col, ins).notes) == expected
        assert PatpopScrub(col, ins).notes.name == f"{col_name}_notes"

    @pytest.mark.parametrize("col_name,expected", pat_pop_error_kv_list)
    def test_pat_pop_delta_counts(self, col_name, expected, mock_pat_pop):
        col = mock_pat_pop[col_name]
        ins = self.__class__.pat_pop_instructions[col_name]
        diff = self.display_check(PatpopScrub(col, ins).clean())
        assert len(diff) == expected

    @pytest.mark.parametrize("col_name,expected", oad_error_kv_list_normal)
    def test_normal_oad_delta_counts(self, col_name, expected, mock_ophthafterdxdate):
        col = mock_ophthafterdxdate[col_name]
        ins = self.__class__.ophthafterdxdate_instructions[col_name]
        diff = self.display_check(PatpopScrub(col, ins).clean())
        assert len(diff) == expected

    @pytest.mark.parametrize("col_name,expected", oad_error_kv_list_va)
    def test_va_oad_delta_counts(self, col_name, expected, mock_ophthafterdxdate):
        col = mock_ophthafterdxdate[col_name]
        ins = self.__class__.ophthafterdxdate_instructions[col_name]
        diff = self.display_check(PatpopScrub(col, ins).clean())
        assert len(diff) == expected
