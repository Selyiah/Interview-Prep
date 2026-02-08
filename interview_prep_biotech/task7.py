#Scenario
#You receive sequencing run data and need to produce a data quality report showing why records are invalid.

import pandas as pd

runs = pd.DataFrame([
    {"run_id": "q01", "run_start": "2026-01-05 09:00", "read_count": "1000000", "status": "Completed"},
    {"run_id": "q02", "run_start": None,              "read_count": "1200000", "status": "Completed"},
    {"run_id": "q03", "run_start": "2026/01/10",      "read_count": "-500",    "status": "Completed"},
    {"run_id": "q04", "run_start": "2026-01-15 10:00","read_count": "800000",  "status": "FAILED"},
    {"run_id": "q05", "run_start": "2026-01-20 11:00","read_count": "invalid", "status": "Completed"},
])


#✅ Your tasks
#Step 1 — Clean types
#normalise status
#convert run_start to datetime (errors="coerce")
#convert read_count to numeric (errors="coerce")

import pandas as pd 
import numpy as np # sql version of case when or pythons version as else if 

runs["status"] = runs["status"].str.lower().str.strip()

runs["run_start"] = pd.to_datetime(runs["run_start"], errors="coerce")

runs["read_count"] = pd.to_numeric(runs["read_count"], errors="coerce")


#Step 2 — Create a quality_issue column
#Create a new column called: quality_issue
#Rules:
#"missing_run_start" if run_start is null
#"invalid_read_count" if read_count is null or ≤ 0
#"failed_run" if status != "completed"
#"valid" if none of the above apply
#(Hint: this is a conditional logic task, not groupby.)

conditions = [
    runs["run_start"].isna(), #isna = is the value missing? whereas notna = is the value present?
    runs["read_count"].isna() | (runs["read_count"] <= 0),
    runs["status"] != "completed"
]

choices = [
    "missing_run_start",
    "invalid_read_count",
    "failed_run"
]

runs["quality_issue"] = np.select(
    conditions,
    choices,
    default="valid"
)



#Step 3 — Produce a summary
#Create a table that shows:
#each quality_issue
#how many runs fall into each category

quality_summary = (
    runs
      .groupby("quality_issue")
      .size()
      .reset_index(name="run_count")
)

quality_summary


