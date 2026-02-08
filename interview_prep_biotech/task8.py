#Scenario
#You receive experiment result data from a lab system.
#Your job is to produce a data quality audit report that explains why records are invalid.
#This time, priority matters.
#Only one issue per row, based on the first rule that matches.

import pandas as pd

experiments = pd.DataFrame([
    {"experiment_id": "e01", "sample_id": "s01", "start_time": "2026-02-01 09:00", "end_time": "2026-02-01 11:00", "reads": "1000000", "status": "Completed"},
    {"experiment_id": "e02", "sample_id": "s02", "start_time": None,              "end_time": "2026-02-01 12:00", "reads": "1200000", "status": "Completed"},
    {"experiment_id": "e03", "sample_id": "s03", "start_time": "2026-02-02 10:00", "end_time": None,              "reads": "900000",  "status": "Completed"},
    {"experiment_id": "e04", "sample_id": "s04", "start_time": "2026-02-03 09:00", "end_time": "2026-02-03 08:30", "reads": "800000",  "status": "Completed"},
    {"experiment_id": "e05", "sample_id": "s05", "start_time": "2026-02-04 14:00", "end_time": "2026-02-04 16:00", "reads": "-500",    "status": "Completed"},
    {"experiment_id": "e06", "sample_id": "s06", "start_time": "2026-02-05 10:00", "end_time": "2026-02-05 12:00", "reads": "700000",  "status": "FAILED"},
])


#✅ Your tasks
#Step 1 — Clean types
#normalise status
#convert start_time and end_time to datetime (errors="coerce")
#convert reads to numeric (errors="coerce")

import pandas as pd 
import numpy as np

experiments["status"] = experiments["status"].str.lower().str.strip()

experiments["start_time"] = pd.to_datetime(experiments["start_time"], errors="coerce")

experiments["end_time"] = pd.to_datetime(experiments["end_time"], errors="coerce")

experiments["reads"] = pd.to_numeric(experiments["reads"], errors="coerce")


#Step 2 — Create quality_issue column
#Add a column called: quality_issue
#Apply rules in this order (priority matters):
#"missing_start_time"
#→ if start_time is null
#"missing_end_time"
#→ if end_time is null
#"end_before_start"
#→ if end_time is earlier than start_time
#"invalid_reads"
#→ if reads is null or ≤ 0
#"failed_experiment"
#→ if status != "completed"
#"valid"
#→ if none of the above apply
#⚠️ Only one issue per row, first match wins.

conditions = [
  experiments["start_time"].isna(),
  experiments["end_time"].isna(), 
  experiments["end_time"] < experiments["start_time"], 
  experiments["reads"].isna() | (experiments["reads"] <= 0), 
  experiments["status"] != "completed"
]

choices = [
  "missing_start_time",
  "missing_end_time",
  "end_before_start", 
  "invalid_reads", 
  "failed_experiment"
]

experiments["quality_issue"] = np.select( #Super simple rule to memorise: Mask = filter (drop rows you don’t want) np.select = label (keep all rows, classify them)
  conditions, 
  choices,
  default="valid"
)


#Step 3 — Produce audit summary
#Create a dataframe showing: quality_issue
#experiment_count (number of experiments per issue)

audit_summary = (
  experiments
  .groupby("quality_issue")
  .size() #count how many rows are in each group
  .reset_index(name="experiment_count")
)

audit_summary

