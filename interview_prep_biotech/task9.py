#Task 7 — Lab Event Processing
#You are given a DataFrame called events with columns:
#event_id (string)
#device_id (string)
#event_time (string, messy)
#event_type (string, messy casing/spaces)
#temperature_c (string, can be invalid)
#status (string, values like OK, FAIL, Unknown, with messy casing/spaces)

#Goal
#Create two outputs:
#events_result
#A DataFrame that contains all original rows plus a new column dq_issue.
#daily_device_summary
#A DataFrame that summarizes valid events by day and device.

import pandas as pd

events = pd.DataFrame([
    {"event_id": "ev01", "device_id": "d01", "event_time": "2026-02-01 09:00", "event_type": "READ",   "temperature_c": "36.5",   "status": "OK"},
    {"event_id": "ev02", "device_id": "d01", "event_time": None,              "event_type": "read ",  "temperature_c": "37.2",   "status": "ok"},
    {"event_id": "ev03", "device_id": "d02", "event_time": "2026/02/01 10:30", "event_type": "WRITE",  "temperature_c": "invalid","status": "OK"},
    {"event_id": "ev04", "device_id": "d02", "event_time": "2026-02-01 11:00", "event_type": "READ",   "temperature_c": "35.0",   "status": "FAIL"},
    {"event_id": "ev05", "device_id": "d03", "event_time": "2026-02-02 08:45", "event_type": "read",   "temperature_c": "-5",     "status": "OK"},
    {"event_id": "ev06", "device_id": "d03", "event_time": "2026-02-02 09:10", "event_type": "WRITE",  "temperature_c": "36.9",   "status": "UNKNOWN"},
])

#Requirements
#Cleaning
#Normalise event_type and status (lowercase + strip)
#Convert event_time to datetime (errors="coerce")
#Convert temperature_c to numeric (errors="coerce")

import pandas as pd
import numpy as np

events["status"] = events["status"].str.lower().str.strip()
events["event_type"] = events["event_type"].str.lower().str.strip() 
events["event_time"] = pd.to_datetime(events["event_time"], errors="coerce")
events["temperature_c"] = pd.to_numeric(events["temperature_c"], errors="coerce")

events_result = events.copy()


#Data quality
#Add a column dq_issue with these rules in priority order:
#missing_event_time if event_time is null
#invalid_temperature if temperature_c is null or temperature_c < 0
#failed_status if status != "ok"
#valid otherwise
#Store this as events_result (keep all rows).

#Valid events
#Define “valid” events as rows where dq_issue == "valid".

conditions = [
  events_result["event_time"].isna(), 
  events_result["temperature_c"].isna() | (events_result["temperature_c"] < 0), 
  events_result["status"] != "ok"
]

choices = [
  "missing_event_time", 
  "invalid_temperature", 
  "failed_status"
]

events_result["dq_issue"] = np.select(
  conditions,
  choices,
  default="valid"
)

#Summary
#Create daily_device_summary grouped by: day (date part of event_time), device_id
#With:
#read_events count of rows where event_type == "read"
#write_events count of rows where event_type == "write"
#avg_temperature mean of temperature_c

# Day key
events_result["day"] = events_result["event_time"].dt.date

# Summary on valid events
valid_events = events_result[events_result["dq_issue"] == "valid"].copy()
valid_events["is_read"] = (valid_events["event_type"] == "read")
valid_events["is_write"] = (valid_events["event_type"] == "write")

daily_device_summary = (
    valid_events
      .groupby(["day", "device_id"])
      .agg(
          read_events=("is_read", "sum"),
          write_events=("is_write", "sum"),
          avg_temperature=("temperature_c", "mean")
      )
      .reset_index()
)

events_result, daily_device_summary





