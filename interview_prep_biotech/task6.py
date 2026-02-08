#Scenario
#Scientists want a monthly throughput report per sample, enriched with sample metadata, and a failure flag per sample.
#You are given:
#sequencing run data
#sample metadata from a separate system

import pandas as pd

# Run-level data
runs = pd.DataFrame([
    {"run_id": "r601", "sample_id": "s100", "run_start": "2026-01-05 09:00", "read_count": "1000000", "status": "Completed"},
    {"run_id": "r602", "sample_id": "s101", "run_start": "2026/01/08 11:30", "read_count": "1200000", "status": "completed"},
    {"run_id": "r603", "sample_id": "s100", "run_start": "2026-01-12 14:00", "read_count": "invalid", "status": "FAILED"},
    {"run_id": "r604", "sample_id": "s102", "run_start": None,              "read_count": "900000",  "status": "completed"},
    {"run_id": "r605", "sample_id": "s103", "run_start": "2026-02-03T10:45","read_count": "1300000", "status": "Completed"},
    {"run_id": "r606", "sample_id": "s101", "run_start": "2026-02-20 16:20","read_count": "1250000", "status": "Aborted"},
])

# Sample metadata
samples = pd.DataFrame([
    {"sample_id": "s100", "project": "Oncology", "organism": "Human"},
    {"sample_id": "s101", "project": "Genomics", "organism": "Mouse"},
    {"sample_id": "s102", "project": "Virology", "organism": "Human"},
    {"sample_id": "s103", "project": "Microbiome", "organism": "Bacteria"},
])


#✅ Your tasks
#Step 1 — Clean runs
#normalise status
#convert run_start to datetime (errors="coerce")
#convert read_count to numeric (errors="coerce")

import pandas as pd

runs["status"] = runs["status"].str.lower().str.strip()

runs["run_start"] = pd.to_datetime(runs["run_start"], errors="coerce") 

runs["read_count"] = pd.to_numeric(runs["read_count"], errors="coerce") 

#Step 2 — Filter valid completed runs
#Create runs_clean keeping only:
#status == "completed"
#run_start not null
#read_count > 0

mask = ( 
  (runs["status"] == "completed") & 
  (runs["run_start"].notna()) & 
  (runs["read_count"] > 0) 
)

runs_clean = runs[mask].copy()

#Step 3 — Derive month
#Add month (start of month) to runs_clean.

runs_clean["month"] = runs_clean["run_start"].dt.to_period("M").dt.to_timestamp()

#Step 4 — Merge
#Left join runs_clean to samples on: sample_id
#Store result as: runs_enriched

runs_enriched = runs_clean.merge(samples, on="sample_id", how="left")


#Step 5 — Aggregate
#Create monthly_sample_summary grouped by: month, sample_id, project
#With:
#total_reads → sum of read_count
#run_count → count of run_id
#Use reset_index().

monthly_sample_summary = ( 
  runs_enriched
      .groupby(["month", "sample_id", "project"])
      .agg(
        total_reads=("read_count", "sum"), 
        run_count=("run_id", "count")
      )
      .reset_index()
)

monthly_sample_summary

#Step 6 — Failure flag
#Create sample_flags with: sample_id
#has_failed_run → True if sample has any run in original runs with:
#status == "failed" OR status == "aborted"
#(helper list pattern again)

failure_flags = runss.loc[runs["status"].isin(["failed", "aborted"]), "sample_id"].unique()

sample_flags = (
  samples[["sample_id"]].drop_duplicates()
      .assign(has_failed_run=lambda df: df["sample_id"].isin(failure_flags))
)


