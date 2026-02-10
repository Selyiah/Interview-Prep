#Problem reminder
#Count how many events happened per day, ignoring None days.

events = [
    ("2026-02-09", "entry"),
    ("2026-02-09", "exit"),
    ("2026-02-10", "entry"),
    (None, "entry"),
]

count {}

for day, event_type in events: 
    if day is None: 
      continue 
    if day not in counts: 
      counts[day] = 0
    counts[day] += 1
  
print(counts)


#Dictionary Grouping (Solo)
#Problem
#Count how many valid events happened per location.

records = [
    ("london", "entry"),
    ("london", "exit"),
    ("paris", "entry"),
    ("london", "entry"),
    (None, "entry"),
    ("paris", "exit"),
]


#Rules
#Ignore records where location is None
#Use:
#for
#if
#a dictionary

count = {}

for location, event_type in records:
    if location is None: 
      continue 
    if location not in counts: 
      counts[location] = 0 
    counts[location] += 1
  
print(counts)



#Problem
#Count how many valid events happened per event type.

records = [
    ("entry", "2026-02-09"),
    ("exit", "2026-02-09"),
    ("entry", "2026-02-10"),
    ("entry", "2026-02-10"),
    (None, "2026-02-10"),
]


#Rules
#Ignore records where event_type is None
#Group per event_type

counts = {}

for event_type, day in records:
    if event_type is None: 
      continue
    if event_type not in count: 
      counts[event_type] = 0 
    counts[event_type] += 1

print(counts)



#Problem
#Count how many valid events happened per day.

records = [
    ("2026-02-09", "entry"),
    ("2026-02-09", "exit"),
    ("2026-02-10", "entry"),
    ("2026-02-10", "entry"),
    ("2026-02-10", None),
    (None, "entry"),
]

#Rules
#Ignore records where:
#day is None, or
#event_type is None
#Group per day

counts = {}

for day, event_type in records:
    if day is None or event_type is None: 
      continue
    if day not in counts: 
      counts[day] = 0 
    counts[day] += 1

print(counts)





#Problem
#Count how many valid records happened per user.

records = [
    ("u1", "login"),
    ("u2", "login"),
    ("u1", "logout"),
    ("u3", "login"),
    (None, "login"),
    ("u2", None),
]


counts = {}

for user_id, action in records: 
    if user_id is None or action is None: 
      continue 
    if user_id not in counts: 
      counts[user_id] = 0
    counts[user_id] += 1

print(counts)



      
