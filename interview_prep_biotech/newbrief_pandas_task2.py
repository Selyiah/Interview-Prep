#Scenario
#You’re working with real-world event data coming from devices. Each row represents a single event.

import pandas as pd

df = pd.DataFrame({
    "device_id": ["d1","d2","d1","d3","d2","d2","d4","d4", None],
    "event_type": ["entry","entry","exit","entry","entry","exit","entry","exit","entry"],
    "location_id": ["l1","l1","l1","l2","l1","l1","l2","l2","l2"],
    "event_time": [
        "2026-02-09T08:15:00Z",
        "2026-02-09T09:00:00Z",
        "2026-02-09T10:30:00Z",
        "2026-02-09T11:45:00Z",
        "2026-02-10T00:10:00Z",
        "2026-02-10T08:00:00Z",
        "2026-02-10T09:30:00Z",
        None,
        "2026-02-10T10:00:00Z"
    ]
})


#Your Task
#Write pandas code that produces a DataFrame with:
#day (YYYY-MM-DD)
#location_id
#entry_events → count of event_type == "entry"
#exit_events → count of event_type == "exit"

#Rules (very interview-realistic)
#Ignore rows where device_id or event_time is null
#Convert event_time to datetime
#Group by day + location_id
#Counts should be separate columns, not rows
#Sort output by day, then location_id


import pandas as pd 

df["event_type"] = df["event_type"].str.lower().str.strip()

df["event_time"] = pd.to_datetime(df["event_time"], utc=True, errors="coerce")

mask = (
  (df["device_id"].notna()) & 
  (df["event_time"].notna()) &
  ((df["event_type"] == "entry") | (df["event_type"] == "exit")
)

df_clean = df[mask].copy()

df_clean["day"] = df_clean["event_time"].dt.strftime("%Y-%m-%d")

df_clean["entry_event"] = (df["event_type"] == "entry").astype(int)
df_clean["exit_event"] = (df["event_type"] == "exit").astype(int)


df_summary (
  df_clean
  .groupby(["day", "location_id"], as_index=False)
  .agg(
    entry_events=("entry_event", "sum"),
    exit_events=("exit_event", "sum"),
  .sort_value(["day", "location_id"]),
  .reset_index(drop=True))

df_clean, df_summary 
