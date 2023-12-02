# clef-data-cleaning
Clef needs data cleaning.
***
The first sheet is PAT_POP.
The recipe needed for PAT_POP can be found in `etls/instructions.py`
- "format"
- "string_intention"
- Optional["val_to_notes"]

And to achieve test coverage, we rely on delta counts obtained from the data_cleaning_summary .xlsx file.

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
```
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
│   ├── processed
|   |   ├── alldxatfirstdxdate_revised.csv
|   |   ├── dxafterdxdate_revised.csv
|   |   ├── ophthafterdxdate_revised.csv
|   |   ├── pat_pop_revised.csv
```

 2. Configure pytest with your IDE (Optional)
 3. Make sure code is pointed at the correct version of data_cleaning_summary. 
## Run script to generate workbook of cleaned sheets
```bash
python clef.py make_workbook
```

## Run script to generate clean sheet (saved to `processed` folder)i
- Format is: <python> <module> <function> <args>
- Args can be [pat_pop, dxafterdxdate, ophthafterdxdate, alldxatfirstdxdate, allmeds] 
```bash
python clef.py make_sheet pat_pop
```
:metal: Thanks for using :musical_score:CLEF