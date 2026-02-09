#Scenario
#You receive device events plus a reference table that maps each device to a model type. You need to produce daily 
#metrics per location and model.

import pandas as pd

events = pd.DataFrame({
    "device_id": ["d1","d2","d1","d3","d2","d5", None, "d4","d4"],
    "location_id": ["l1","l1","l1","l2","l1","l2","l2","l2","l2"],
    "event_time": [
        "2026-02-09T07:30:00Z",
        "2026-02-09T09:00:00Z",
        "2026-02-09T10:30:00Z",
        "2026-02-09T11:45:00Z",
        "2026-02-10T08:00:00Z",
        "2026-02-10T09:30:00Z",
        "2026-02-10T10:00:00Z",
        None,
        "2026-02-10T12:00:00Z"
    ]
})

devices = pd.DataFrame({
    "device_id": ["d1","d2","d3","d4"],
    "model": ["minion","minion","promethion","minion"]
})


#Your Task
#Produce a DataFrame with: 
#day (YYYY-MM-DD)
#location_id
#model
#total_events → count of events
#unique_devices → number of distinct devices contributing events

#Rules
#Ignore rows in events where device_id or event_time is null
#Parse event_time into datetime
#Left join events to devices on device_id
#Any events whose device_id is not found in the devices table should have model set to "unknown"
#(In this data, device "d5" is not in the mapping — that’s intentional)
#Group by day + location_id + model
#Sort by day, then location_id, then model
#Output should be clean (no index columns)

import pandas as pd 

devices["model"] = device["model"].str.lower().str.strip()

events["event_time"] = pd.to_datetime(events["event_time"], utc=True, errors="coerce")

mask = (
  (events["device_id"].notna()) & 
  (events["event_time"].notna()) 
)

events_clean = events[mask].copy()

events_clean["day"] = events_clean["event_time"].dt.strftime("%Y-%m-%d")

events_devices = events_clean.merge(devices, on="device_id", how="left")

events_devices["model"] = events_devices["model"].fillna("unknown")

events_devices_summary = (
  events_devices
  .groupby(["day", "location_id", "model"], as_index=False)
  .agg(
    total_events=("event_time", "count"),
    unique_devices=("device_id", "nunique"))
  .sort_values(["day", "location_id", "model"])
  .reset_index(drop=True)
)

events_clean, events_devices, event_devices_summary 
  



