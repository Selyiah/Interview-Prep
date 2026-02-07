#🧬 Practice Task 3 — Instrument Reliability Summary
#Scenario
#Scientists want to understand instrument reliability over time.
#You’re given run data and instrument metadata.

#Your job is to clean the data, derive a month, flag failures, and produce a monthly reliability summary.

import pandas as pd

runs = pd.DataFrame([
    {"run_id": "r301", "instrument_id": "inst01", "run_start": "2026-01-02 08:00", "read_count": "1000000", "status": "Completed"},
    {"run_id": "r302", "instrument_id": "inst01", "run_start": "2026-01-10 09:30", "read_count": "900000",  "status": "FAILED"},
    {"run_id": "r303", "instrument_id": "inst02", "run_start": "2026/01/15 13:00", "read_count": "1100000", "status": "completed"},
    {"run_id": "r304", "instrument_id": "inst02", "run_start": None,              "read_count": "1050000", "status": "completed"},
    {"run_id": "r305", "instrument_id": "inst03", "run_start": "2026-02-05T10:00","read_count": "invalid", "status": "Completed"},
    {"run_id": "r306", "instrument_id": "inst01", "run_start": "2026-02-20 16:45","read_count": "1200000","status": "Aborted"},
])

instruments = pd.DataFrame([
    {"instrument_id": "inst01", "model": "NovaSeq",  "location": "Oxford"},
    {"instrument_id": "inst02", "model": "MiSeq",    "location": "Cambridge"},
    {"instrument_id": "inst03", "model": "NextSeq",  "location": "Oxford"},
])


#✅ Your tasks
#Step 1 — Clean runs
#Normalise status
#Convert run_start to datetime (errors="coerce")
#Convert read_count to numeric (errors="coerce")

import pandas as pd 

runs["status"] = runs["status"].str.lower().str.strip()

runs["run_start"] = pd.to_datetime(runs["run_start"], errors="coerce") 

runs["read_count"] = pd.to_numeric(runs["read_count"], errors="coerce")


#Step 2 — Filter to valid completed runs
#Keep only:
#status == "completed"
#run_start not null
#read_count > 0
#Store as: runs_clean

mask = (
  (runs["status"] == "completed") & 
  (runs["run_start"].notna()) & 
  (runs["read_count"] > 0) 
)

runs_clean = runs[mask].copy()

#Step 3 — Derive month
#Add: month as start of month, derived from run_start.

runs_clean["month"] = runs_clean["run_start"].dt.to_period("M").dt.to_timestamp()

#Step 4 — Join instrument metadata
#Left join runs_clean to instruments on: instrument_id
#Store as: runs_enriched

runs_enriched = runs_clean.merge(instruments, on="instrument_id", how="left")

#Step 5 — Aggregate
#Create: monthly_reliability
#Grouped by: month, location
#With:
#total_reads → sum of read_count
#run_count → count of run_id

monthly_reliability = ( 
  runs_enriched
      .groupby(["month", "location"])
      .agg(
        total_reads=("read_count", "sum"),
        run_count=("run_id", "count)
      )
  .reset_index()

)

monthly_reliability 


#Step 6 — Instrument failure flag
#Create: instrument_flags
#With: instrument_id
#has_failed_run → True if the instrument has any run in the original runs table with:
#status == "failed" OR status == "aborted"
#(Hint: same pattern as failed_samples, just different entity.)

instrument_failure_flag = runs.loc[runs["status"].isin(["failed", "aborted"]), "instrument_id"].unique()

instrument_flags = (
  intstruments(["instrument_id])
      .assign(has_failed_runs=instruments["instrument_id"].isin(instrument_failure_flag))







