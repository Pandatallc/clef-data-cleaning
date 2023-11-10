from etls.instructions import pat_pop as ins
from etls.sheet_cleaner import SheetCleaner

import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)

if __name__ == "__main__":
    
    s = SheetCleaner("pat_pop", ins)
    df = s.get_clean()
    df.to_csv("data/processed/pat_pop_revised.csv")