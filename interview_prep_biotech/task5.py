#Scenario
#You’re analysing sequencing jobs to understand monthly throughput by study, plus whether each study has ever experienced failures.

import pandas as pd

job_logs = pd.DataFrame([
    {"job_id": "j401", "specimen_id": "sp10", "study": "Oncology", "start_time": "2026-01-03 09:10", "reads": "1200000", "state": "Completed"},
    {"job_id": "j402", "specimen_id": "sp11", "study": "Oncology", "start_time": "2026/01/08 11:00", "reads": "1150000", "state": "FAILED"},
    {"job_id": "j403", "specimen_id": "sp12", "study": "Virology", "start_time": "2026-01-15 14:30", "reads": "980000",  "state": "completed"},
    {"job_id": "j404", "specimen_id": "sp12", "study": "Virology", "start_time": None,              "reads": "970000",  "state": "completed"},
    {"job_id": "j405", "specimen_id": "sp13", "study": "Genomics", "start_time": "2026-02-02T10:00","reads": "invalid", "state": "Completed"},
    {"job_id": "j406", "specimen_id": "sp14", "study": "Genomics", "start_time": "2026-02-18 16:20","reads": "1300000","state": "Aborted"},
])


#✅ Your tasks (same logic, new names)
#Step 1 — Clean job_logs
#Normalise state
#Convert start_time to datetime (errors="coerce")
#Convert reads to numeric (errors="coerce")

import pandas as pd

job_logs["state"] = job_logs["state"].str.lower().str.strip()

job_logs["start_time"] = pd.to_datetime(job_logs["start_time"], errors="coerce")

job_logs["reads"] = pd.to_numeric(job_logs["reads"], errors="coerce")


#Step 2 — Filter valid completed jobs
#Keep only:
#state == "completed"
#start_time not null
#reads > 0
#Store as: jobs_clean

mask = (
  (job_logs["state"] == "completed") & 
  (job_logs["start_time"].notna()) & 
  (job_logs["reads"] > 0) 
)
jobs_clean = job_logs[mask].copy()

#Step 3 — Derive month
#Add: month as the start of the month, derived from start_time.

jobs_clean["month"] = job_clean["start_time"].dt.to_period("M").dt.to_timestamp()


#Step 4 — Aggregate throughput
#Create: monthly_study_throughput
#Grouped by: month, study
#With:
#total_reads → sum of reads
#job_count → count of job_id
#Use reset_index().

monthly_study_throughput = ( 
  jobs_clean
      .groupby(["month", "study"])
      .agg(
        total_reads=("reads", "sum"),
        job_count=("job_id", "count")
      )
      .reset_index()

)

monthly_study_throughput 

#Step 5 — Study failure flag
#Create: study_flags
#With: study
#has_failed_job → True if the study has any job in the original job_logs table with:
#state == "failed" OR state == "aborted"
#(Hint: exact same helper-variable pattern — just different column names.)

study_failure_flag = job_logs.loc[job_logs["state"].isin(["failed", "aborted"]), "study"].unique()

study_flags = (
  job_logs[["study"]].drop_duplicates()
      .assign(has_failed_job=lamba df: df["study"].isin(study_failure_flag))
)






