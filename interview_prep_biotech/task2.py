# raw data 
import pandas as pd

runs = pd.DataFrame([
    {"run_id": "r101", "instrument_id": "instA", "run_start": "2026-01-03 10:15:00", "read_count": "1500000", "error_rate": "0.01", "status": "Completed"},
    {"run_id": "r102", "instrument_id": "instA", "run_start": "2026/01/05 09:30",     "read_count": "1400000", "error_rate": "0.02", "status": "completed"},
    {"run_id": "r103", "instrument_id": "instB", "run_start": "07-01-2026 14:00",     "read_count": "invalid", "error_rate": "0.05", "status": "FAILED"},
    {"run_id": "r104", "instrument_id": "instB", "run_start": None,                  "read_count": "1300000", "error_rate": "0.03", "status": "completed"},
    {"run_id": "r105", "instrument_id": "instC", "run_start": "2026-02-02T11:45:00",  "read_count": "1600000", "error_rate": "invalid", "status": "Completed"},
    {"run_id": "r106", "instrument_id": "instA", "run_start": "2026-02-10 16:20:00",  "read_count": "1550000", "error_rate": "0.015", "status": "Aborted"},
])

#Step 1 — Clean the data
# Normalise status (lowercase + strip) 
#Convert run_start to datetime (errors="coerce")
#Convert read_count to numeric (errors="coerce")
#Convert error_rate to numeric (errors="coerce")

import pandas as pd 

runs["status"] = runs["status"].str.lower().str.strip()

runs["run_start"] = pd.to_datetime(runs["run_start"], errors="coerce")

runs["read_count"] = pd.to_numeric(runs["read_count"], errors="coerce")

runs["error_rate"] = pd.to_numeric(runs["error_rate"], errors="coerce")

#Step 2 — Filter to valid runs

#Keep only rows where:
#status == "completed"
#run_start is not null
#read_count > 0
#error_rate is not null

#Store the result as:
#runs_clean

runs_clean = runs[
    (runs["status"] == "complete") &
    (runs["run_start"].notna()) & 
    (runs["read_count"] > 0) & 
    (runs["error_rate"].notna()) 
]


#Step 3 — Derive month
#Add a column:
#month
#Derived from run_start, representing the start of the month.

runs_clean["month"] = runs_clean["run_start"].dt.to_period("M").dt.to_timestamp()

#Step 4 — Aggregate
#Create a dataframe called:
#quality_summary
#Grouped by:
#month, instrument_id

quality_summary = (
    runs_clean 
        .groupby(["month", "instrument_id"]),
        .agg(
          total_reads =("read_count", "sum"),
          avg_error_rate=("error_rate", "mean"),
          run_count =("run_id", "count") 
    )
    .reset_index()

)

quality_summary

#With: 
#total_reads → sum of read_count
#avg_error_rate → mean of error_rate
#run_count → count of run_id

#Use reset_index() so the result is a clean table.
