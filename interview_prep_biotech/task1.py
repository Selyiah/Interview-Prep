# Mini task 
# You have a dataframe runs with: run_start, read_count, status, instrument_id
# Goal: To create a dataframe summary grouped by month and instrument_id with:
# - total_reads = sum of read_count for completed runs only
# - run_count = number of completed runs
# Contstraints: Parse run_start to dateime, Convert read_count to numeric, keep only rows where status == completed (case sensitive), run_start is not null, read_count > 0

# Starter data example 
import pandas as pd 

runs = pd.DataFrame([
  {"run_id": "r001", "instrument_id": "inst01", "run_start": "2026-01-05 09:12:00", "read_count": "1200000", "status": "completed"},
  {"run_id": "r002", "instrument_id": "inst01", "run_start": "2026/01/06 11:05", "read_count": "950000", "status": "COMPLETED"}, 
  {"run_id": "r003", "instrument_id": "inst02", "run_start": "06-02-2026 08:00", "read_count": "invalid", "status": "failed"},
  {"run_id": "r004", "instrument_id": "inst02", "run_start": None, "read_count": "500000", "status": "completed"},
  {"run_id": "r005", "instrument_id": "inst03", "run_start": "2026-02-15T14:30:00", "read_count": "0", "status": "completed"}, 
  {"run_id": "r006", "instrument_id": "inst01", "run_start": "2026-02-01 10:00:00", "read_count": "1100000", "status": "aborted"},
])

# Answer below

import pandas as pd #library 

# 1. Normalise status - make the values consistent so comparisons work reliably e.g. "completed", "COMPLETED", " Completed ", "Completed ". In Python they are different strings, so filtering can break.
# Normalising = turning all of those into the same exact form e.g. "completed". 
# why runs? runs is a pandas DataFrame (a table) and "Status" is a column in that table.
# runs[status] = means "replace the status column with this cleaned version". So this run essentially overwrites the column with a clean version of itself. 
# runs[status] appears on both sides: left side = where to store/where the result goes and right side = the cleaned values. .str = strings, lower = lowercase, strip() removes leading and trailing whitespace (spaces, tabs, newlines)
runs["status"] = runs["status"].str.lower().str.strip()

#2. Parse run start to datetime - errors="coerce" means if you cannot convert a value into a datetime, do not fail but convert to NaT (Not a Time). 
runs["run_start"] = pd.to_datetime(runs["run_start"], errors="coerce")

#3. Convert read_count to numeric - will default to float numbers when there are nulls in the dataset. If int is required then specify later to .astype("int") but only after removing nulls.
runs["read_count"] = pd.to_numeric(runs["run_start"], errors="coerce") 

#4. Filter to valid completed runs - boolean indexing is what this below is called. Notna means is this value not missing? so it will return True is the value exists, False if it's missing. 
runs_clean = runs[
    (runs["status"] == "completed") & # keeps completed runs
    (runs["run_start"].notna()) & # drops rows with missing timestamps
    (runs["read_count"] > 0) # drop empty or meaningless runs (above 0). 
] 

# & = AND, | = OR, ~ = NOT (bitwise operators)

# 5. Derive month column - can only use .dt on datetime columns 
runs_clean["month"] = runs_clean["run_start"].dt.to_period("M").dt.to_timestamp()

# 6. Aggregate
summary = (
  runs_clean # the original table being used to produce the summary. 
      .groupby(["month", "instrument_id"])
      .agg(
          total_reads=("read_count", "sum"), 
          run_count=("run_id", "count")
      )
      .reset_index() # moves them back into normal columns to use like a normal table 
)

summary 



# answer without notes 

import pandas as pd 

runs["status"] = runs["status"].str.lower().str.strip()

runs["run_start"] = pd.to_datetime(runs["run_start"], errors="coerece")

run["read_count"] = pd.to_numeric(runs["run_start"], errors="coerece")

runs_clean = runs[
    (runs["status"] == "completed") &
    (runs["run_start"].notna()) & 
    (runs["read_count"] > 0)
]

runs_clean["month"] = runs_clean["run_start"].dt.to_period.("M").dt.to_timestamp()

summary = (
  runs_clean
      .groupby(["months", "instrument_id"])
      .agg (
        total_reads=("read_count", "sum"),
        run_count=("run_id", "count")
      )
      .reset_index()

)

summary
  
