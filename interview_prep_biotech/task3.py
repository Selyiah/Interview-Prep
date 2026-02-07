# raw data 
import pandas as pd

runs = pd.DataFrame([
    {"run_id": "r201", "sample_id": "s001", "run_start": "2026-01-04 09:00:00", "read_count": "1200000", "status": "Completed"},
    {"run_id": "r202", "sample_id": "s002", "run_start": "2026/01/06 11:30",     "read_count": "950000",  "status": "completed"},
    {"run_id": "r203", "sample_id": "s002", "run_start": "07-01-2026 14:00",     "read_count": "invalid", "status": "FAILED"},
    {"run_id": "r204", "sample_id": "s003", "run_start": None,                  "read_count": "800000",  "status": "completed"},
    {"run_id": "r205", "sample_id": "s004", "run_start": "2026-02-03T10:45:00",  "read_count": "1100000", "status": "Completed"},
    {"run_id": "r206", "sample_id": "s001", "run_start": "2026-02-15 16:20:00",  "read_count": "1000000", "status": "Aborted"},
])

samples = pd.DataFrame([
    {"sample_id": "s001", "project": "Cancer",     "organism": "Human"},
    {"sample_id": "s002", "project": "Genomics",   "organism": "Mouse"},
    {"sample_id": "s003", "project": "Virology",   "organism": "Human"},
    {"sample_id": "s004", "project": "Microbiome", "organism": "Bacteria"},
])

#Your tasks
#Step 1 — Clean runs
#Normalise status (lowercase + strip)
#Convert run_start to datetime (errors="coerce")
#Convert read_count to numeric (errors="coerce")
import pandas as pd

runs["status"] = runs["status"].str.lower().str.strip()

runs["run_start"] = pd.to_datetime(runs["run_start"], errors="coerce")

runs["read_count"] = pd.to_numeric(runs["read_count"], errors="coerce")

#Step 2 — Filter to valid completed runs
#Keep only rows where:
#status == "completed"
#run_start is not null
#read_count > 0
#Store result as: runs_clean
# Mask is a boolean series meaning it has the same number of rows as 'runs'. Mask answers should I keep this row?

mask = (
  (runs["status"] == "completed") & 
  (runs["run_start"].notna()) & 
  (runs["read_count"] > 0)
)

runs_clean = runs[mask].copy() #run[mask] is boolean indexing meaning - give me only the rows of runs where mask is true 
#.copy() gives a clean independent dataframe 

#to sum up: 
#mask = the rule
#runs[mask] = applying the rule
#.copy() = making it safe and independent
#to prevent ambigious ownership of data so when making any changes to runs_clean, runs remains unchanged 


#Step 3 — Derive month
#Add a column:
#month
#Representing the start of the month, derived from run_start.

runs_clean["month"] = runs_clean["run_start"].dt.to_period("M").dt.to_timestamp()

#Step 4 — Join sample metadata
#Left join runs_clean to samples on:
#sample_id
#Store result as:
#runs_enriched

runs_enriched = runs_clean.merge(samples, on="sample_id", how="left")

#Step 5 — Aggregate
#Create a dataframe: monthly_summary
#Grouped by: month, project
#With: 
#total_reads → sum of read_count
#run_count → count of run_id
#Use reset_index().

monthly_summary = (
  runs_enriched
    .groupby(["month", "project"]) 
    .agg(
      total_reads("read_count", "sum"),
      run_count("run_id", "count")
    )
.reset_index()

)

monthly_summary


#Step 6 — Sample quality flag (small twist)
#Create a dataframe: sample_flags
#With: sample_id
#has_failed_run → True if the sample has any run in runs (original table) with:
#status == "failed" OR status == "aborted"
#(Hint: you do not need groupby for this if you think carefully.)

#.loc means select rows and columns at the same time 
#.unique removes duplicates 

failed_samples = runs.loc[runs["status"].isin(["failed", "aborted"]), "sample_id"].unique()

sample_flags = (
    samples[["sample_id"]]
      .assign(has_failed_runs=samples["sample_id"].isin(failed_samples))
)

#.assign means add a new column 

