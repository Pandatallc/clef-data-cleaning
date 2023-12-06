import logging
from pathlib import Path
from xlwt.Workbook import *
from pandas import ExcelWriter

from etls.instructions import instructions
from etls.sheet_handler import SheetHandler

import sys
import os

conf_path = os.getcwd()
sys.path.append(conf_path)

fh = logging.StreamHandler(sys.stdout)
logger = logging.getLogger()
logger.addHandler(fh)
logger.setLevel(logging.INFO)


sheet_names = {
    "pat_pop": ("pat_pop", "PAT_POP"),
    "ophthafterdxdate": ("ophthafterdxdate", "ophth after DXDate"),
    "dxafterdxdate": ("dxafterdxdate", "DX after DXDate"),
    "alldxatfirstdxdate": ("alldxatfirstdxdate", "All DX at FirstDXDate"),
    "allmeds": ("allmeds", "All MEDs"),
}


def make_workbook():
    with ExcelWriter(Path("data", "processed", "CLEAN_MASTER_FILE.xlsx")) as writer:
        for sheet_name in sheet_names.values():
            s = SheetHandler(sheet_name, instructions)
            clean_sheet = s.get_clean_sheet()
            clean_sheet.to_excel(writer, sheet_name=f"{sheet_name[1]}", index=False)
    logger.info("\N{basket} Exported Workbook with Clean Sheets")


def make_sheet(sheet):
    sheet_name = sheet_names[sheet]
    s = SheetHandler(sheet_name, instructions)
    clean_sheet = s.get_clean_sheet()
    clean_sheet.to_csv(f"data/processed/{sheet}_revised.csv")
    logger.info("\N{basket} Exported clean sheet as .csv in data/processed directory.")

def refresh_all():
    with ExcelWriter(Path("data", "processed", "CLEAN_MASTER_FILE.xlsx")) as writer:
        for sheet_name in sheet_names.values():
            s = SheetHandler(sheet_name, instructions)
            clean_sheet = s.get_clean_sheet()
            clean_sheet.to_csv(f"data/processed/{sheet_name[0]}_revised.csv")
            clean_sheet.to_excel(writer, sheet_name=f"{sheet_name[1]}", index=False)
    logger.info("\N{basket} Exported Workbook with Clean Sheets")
 


if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])
    logger.info("\N{sign of the horns} Thanks for using \N{musical score}CLEF")
