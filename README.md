# :musical_score:CLEF
Data cleaning parameters per column: `etls/instructions.py`

***
## Set up environment 
``` python
python -m venv .venv
.venv/Scripts/activate #windows
source .venv/bin/activate #mac
pip install -r requirements.txt
```
Manual steps
1. Create a data folder in the root directory
```python
├── data
│   ├── raw
│   │   ├── ccf_apellis_data_cleaning_summary_20231120.xlsx
|   |   ├── MASTER FILE.xlsx
│   ├── interim 
|   |   ├── alldxatfirstdxdate.csv
|   |   ├── allmeds.csv
|   |   ├── dxafterdxdate.csv
|   |   ├── ophthafterdxdate.csv
|   |   ├── pat_pop.csv
│   ├── processed   # to be produced by CLEF 
|   |   ├── alldxatfirstdxdate_revised.csv
|   |   ├── dxafterdxdate_revised.csv
|   |   ├── ophthafterdxdate_revised.csv
|   |   ├── pat_pop_revised.csv
```

 2. Configure pytest with your IDE
 3. Make sure code is pointed at the correct version of data_cleaning_summary. 
    - edit .conftest to reflect new delta counts
    - edit [`etls.sheets.va_cols.py L28`](https://github.com/Pandatallc/clef-data-cleaning/blob/feature/CLEF-003_clean_ophthafterdxdate/etls/sheets/va_cols.py#L28)
## Run script to generate workbook of cleaned sheets
```bash
python clef.py make_workbook
```
```bash
:basket: Exported Workbook of Clean Sheets
```

## Run script to generate clean sheet (saved to `processed` folder)i
- Format is: `python` `module` `function` `args`
- Args can be [pat_pop, dxafterdxdate, ophthafterdxdate, alldxatfirstdxdate, allmeds] 
```bash
python clef.py make_sheet pat_pop
```
```bash
:basket: Exported clean sheet as .csv in data/processed directory
```
:metal: Thanks for using :musical_score:CLEF