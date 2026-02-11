#Problem
#You are given event records:

records = [
    ("u1", "purchase", "2026-06-01T09:00:00Z"),
    ("u2", "purchase", "2026-06-01T09:30:00Z"),
    ("u1", "purchase", "2026-06-01T10:00:00Z"),
    ("u3", "refund",   "2026-06-02T08:00:00Z"),
    ("u2", "purchase", None),
    (None, "purchase", "2026-06-02T09:00:00Z"),
    ("u3", "purchase", "2026-06-02T10:00:00Z"),
]

#Task
#Return the number of unique users who made a "purchase" per day.

#Rules
#Ignore rows where:
#user_id is None
#timestamp is None
#Only count "purchase" events
#Extract day using slicing

def unique_purchase_per_day(records):
  unique_purchases = {}

  for user_id, action, timestamp in records: 
    if user_id is None or action is None or timestamp is None: 
      continue 
    if action != "purchase":
      continue

    day = timestamp[:10]

    if day not in unique_purchases:
      unique_purchases[day] = set()
    unique_purchases[day].add(user_id)

  return {day: len(users) for day, users in unique_purchases.item()}





#Problem
import pandas as pd

df = pd.DataFrame({
    "device_id": ["d1","d2","d1","d3",None,"d2","d4"],
    "location_id": ["l1","l1","l1","l2","l2","l1","l2"],
    "event_type": ["entry","entry","exit","entry","exit","exit","entry"],
    "event_time": [
        "2026-06-01T07:30:00Z",
        "2026-06-01T08:45:00Z",
        "2026-06-01T09:00:00Z",
        "2026-06-02T10:15:00Z",
        "2026-06-02T08:00:00Z",
        None,
        "2026-06-02T11:00:00Z",
    ]
})


#Task
#Produce a DataFrame with:
#day
#location_id
#total_events
#unique_devices

#Rules
#Ignore rows where:
#device_id is null
#event_time is null
#Convert event_time to datetime
#Extract day
#Group by day and location_id
#Clean final output (no weird index columns)

import pandas as pd 

df["event_type"] = df["event_type"].str.lower().str.strip()

df["event_time"] = pd.to_datetime(df["event_time"], utc=True, errors="coerce")

mask = (
  (df["device_id"].notna()) & 
  (df["event_time"].notna()) 
)

df_clean = df[mask].copy()

df_clean["day"] = df_clean["event_time"].dt.strftime("%Y-%m-%d")

df_summary = (
  df_clean
  .groupby(["day", "location_id"]), as_index(False)
  .agg(
    total_events=("event_time", "count"),
    unique_devices=("device_id", "nunique"))
  .sort_values(["day", "location_id"]) 
  .reset_index(drop=True)
)

df_clean, df_summary



