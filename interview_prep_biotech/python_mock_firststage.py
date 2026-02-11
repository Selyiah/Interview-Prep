#Part 1 — Python Fundamentals (≈15 minutes)
#Problem
#You are given a list of event records.
#Each record contains:
#user_id
#timestamp (ISO-8601 string)

records = [
    ("u1", "2026-02-09T09:15:00Z"),
    ("u2", "2026-02-09T10:30:00Z"),
    ("u1", "2026-02-09T11:45:00Z"),
    ("u3", "2026-02-10T08:00:00Z"),
    (None, "2026-02-10T09:00:00Z"),
    ("u2", None),
    ("u4", "2026-02-10T12:30:00Z"),
]

#Task
#Write a Python function that returns the number of unique active users per day.
#Rules
#Ignore records where:
#user_id is None, or timestamp is None
#Group per day (YYYY-MM-DD)
#Use pure Python
#for
#if
#dictionaries
#sets (if needed)

unique_active_users_per_day = {}

for user_id, timestamp in records:
    if user_id is None or timestamp is None:
      continue 
    day = timestamp[:10]
    if day not in unique_active_users_per_day:
      unique_active_users_per_day[day] = 0
    unique_active_users_per_day[day] += 1
  
    print(unique_active_users_per_day)



def unique_active_users_per_day(records):
    users_by_day = {}

    for user_id, timestamp in records:
        if user_id is None or timestamp is None:
            continue

        day = timestamp[:10]

        if day not in users_by_day:
            users_by_day[day] = set()

        users_by_day[day].add(user_id)

    return {day: len(users) for day, users in users_by_day.items()}





#Part 2 — pandas / DataFrame Task (≈15 minutes)
#Problem
#You are analysing device events.


import pandas as pd

df = pd.DataFrame({
    "device_id": ["d1","d1","d2","d3",None,"d2","d4"],
    "location_id": ["l1","l1","l1","l2","l2","l1","l2"],
    "event_type": ["entry","exit","entry","entry","exit","exit","entry"],
    "event_time": [
        "2026-02-09T07:30:00Z",
        "2026-02-09T08:45:00Z",
        "2026-02-09T09:00:00Z",
        "2026-02-09T10:15:00Z",
        "2026-02-10T08:00:00Z",
        None,
        "2026-02-10T11:00:00Z",
    ]
})



#ask
#Produce a DataFrame with one row per day and location, containing:
#day
#location_id
#total_events
#unique_devices

#Rules
#Ignore rows where:
#device_id is null, or event_time is null
#Convert event_time to datetime
#Create day (YYYY-MM-DD)
#Group by day + location_id
#Output should be clean (no index columns)

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
  .groupby(["day", "location_id").as_index(False)
  .agg(
    total_events=("event_time", "count"),
    unique_devices=("device_id", "nunique"))
  .sort_values(["day", "location_id"])
  .reset_index(drop=True)
)

df_clean, df_summary











#Problem
#Return the number of unique users per day.

records = [
    ("u1", "2026-04-01T09:00:00Z"),
    ("u2", "2026-04-01T10:00:00Z"),
    ("u1", "2026-04-01T11:00:00Z"),
    ("u3", "2026-04-02T08:00:00Z"),
    ("u2", "2026-04-02T09:30:00Z"),
    ("u3", "2026-04-02T10:15:00Z"),
    (None, "2026-04-02T11:00:00Z"),
    ("u4", None),
]



#Rules
#Ignore rows where:
#user_id is None, OR timestamp is None
#Extract day using slicing (timestamp[:10])

def unique_users_per_day(records):
  users_per_day = {}

  for user_id, timestamp in records:
    
    if user_id is None or timestamp is None:
      continue 

    day = timestamp[:10] 

    if day not in users_per_day: 
      users_per_day[day] = set()
    users_per_day[day].add(user_id)

  return {day: len(users) for day, users in users_per_day.items()}






#Problem
#You are given event records:

records = [
    ("u1", "login", "2026-05-01T09:00:00Z"),
    ("u2", "login", "2026-05-01T09:30:00Z"),
    ("u1", "logout", "2026-05-01T10:00:00Z"),
    ("u3", "login", "2026-05-02T08:00:00Z"),
    ("u2", "login", None),
    (None, "login", "2026-05-02T09:00:00Z"),
    ("u3", "login", "2026-05-02T10:00:00Z"),
]


#Task
#Return the number of unique users who performed a "login" action per day.

#Rules
#Ignore rows where:
#user_id is None
#timestamp is None
#Only count "login" events
#Extract day using timestamp[:10]

def unique_users_per_login(records):
  unique_logins = {}
     for user_id, action, timestamp in records: 
       
       if user_id is None or timestamp is None:
         continue 

       day = timestamp[:10]

       if day not in unique_logins:
         unique_logins[day] = set()
       unique_logins[day].add(user_id)

     return {day: len(day) for day, action in unique_logins.items()}





#Problem
#Return the number of unique devices per location.


records = [
    ("l1", "d1", "2026-02-11T09:00:00Z"),
    ("l1", "d2", "2026-02-11T09:05:00Z"),
    ("l1", "d1", "2026-02-11T09:10:00Z"),
    ("l2", "d3", "2026-02-11T10:00:00Z"),
    ("l2", None, "2026-02-11T10:05:00Z"),
    (None, "d4", "2026-02-11T10:10:00Z"),
    ("l2", "d3", None),
    ("l2", "d5", "2026-02-11T10:15:00Z"),
]



#Rules
#Ignore records where location is None OR device_id is None OR timestamp is None
#Group per location
#Count unique devices per location

def unique_devices_per_location(records):
  unique_devices = {}

  for location, device_id, timestamp in records: 
    if location is None or device_id is None or timestamp is None:
      continue
    day = timestamp[:10]

    if location not in unique_devices:
      unique_devices[location] = set()
    unique_devices[location].add(device_id)

  return {location: len(location) for location, device_id in unique_devices.items()}


