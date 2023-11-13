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
data
    - raw
        - MASTER FILE.xlsx # Manually copied from Dropbox
    - interim
        - pat_pop.csv # will need to create this with pandas, see notebook.
    - processed
 2. Configure pytest with your IDE
## Run script
```bash
python pat_pop_script.py
```
