#New Task 1 Variant (your turn)
#Problem
#You’re given records of (device_id, timestamp) where timestamp may be:
#"2026-02-09 10:15:00" (space format)
#"2026-02-09T10:15:00Z" (ISO format)
#or None
#Write a function that returns unique active devices per day, as a dict.

Input
records2 = [
    ("d1", "2026-02-09 10:15:00"),
    ("d2", "2026-02-09T11:00:00Z"),
    ("d1", "2026-02-09T12:30:00Z"),
    ("d3", None),
    ("d2", "2026-02-10 00:01:00"),
    ("d4", "2026-02-10T09:00:00Z"),
    ("",   "2026-02-10T10:00:00Z"),   # invalid device_id (empty string)
]

#Rules
#Ignore invalid device_id (None or empty string) and invalid timestamp (None/empty)
#Extract day as "YYYY-MM-DD" from either timestamp format
#Hint: day is still the first 10 chars in both formats

Expected output
{
  "2026-02-09": 2,   # d1,d2
  "2026-02-10": 2    # d2,d4
}

#Your task
#Write a function:
#def unique_devices_per_day(records2):    ...

#def = defining a function 

def unique_devices_per_day(records2):
    devices_per_day = {}
    for device_id, timestamp in records: #go through the list one item at a time 
      if not device_id or not timestamp:
        continue


    day = timestamp[:10]

    if day not in devices_per_day:
      devices_per_day[day] = set()

    devices_per_day[day].add(device_id)
  
result = {}
for day, devices in devices_per_day.items():
  results[day] = len(users)

return result



