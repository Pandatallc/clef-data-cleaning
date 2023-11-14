from etls.instructions import instructions
from etls.sheet_cleaner import SheetCleaner

import sys
import os

conf_path = os.getcwd()
sys.path.append(conf_path)

if __name__ == "__main__":
    ## clean pat_pop
    # s = SheetCleaner("pat_pop", instructions)
    # df = s.get_clean()
    # df.to_csv("data/processed/pat_pop_revised.csv")

    # clean dxafterdxdate
    s = SheetCleaner("dxafterdxdate", instructions)
    df = s.get_clean()
    df.to_csv("data/processed/dxafterdxdate_revised.csv")
