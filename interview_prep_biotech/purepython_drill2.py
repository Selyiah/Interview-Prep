#Task A — Loop + Conditionals ONLY
#Problem
#Print values that are: 
#not None
#greater than 10
#even

values = [None, 4, 10, 12, 15, 20, -2, 22]

for v in values:
   if v is None:
     continue 
   if v <= 10:
     continue 
   if v % 2 != 0:
     continue 

print(v)



#Task B — Dictionary Grouping
#Problem
#Count how many valid records happened per category.

records = [
    ("food", 10),
    ("travel", 50),
    ("food", 20),
    ("books", 15),
    (None, 30),
    ("travel", None),
    ("food", 5),
]

#Rules
#Ignore records where:
#category is None, or
#amount is None
#Group per category

counts = {}

for category, amount in records:
    if category is None or amount is None:
      continue 
    if category not in counts:
      counts[category] = 0
    counts[category] += 1

print(counts)





#Task A — Loop + Conditionals ONLY
#Problem

#Print values that are:
#not None
#negative
#odd

values = [None, -1, -2, -3, 0, 4, 7, -5]

for v in values:
  if v is None:
    continue 
  if v >= 0:
    continue 
  if v % 2 == 0: 
    continue 
  
  print(v)






#Task B — Dictionary Grouping
#Problem

#Count how many valid actions happened per user.

records = [
    ("u1", "login"),
    ("u2", "login"),
    ("u1", "logout"),
    ("u3", None),
    (None, "login"),
    ("u2", "logout"),
    ("u2", "login"),
]

#Rules
#Ignore records where:
#user is None, or
#action is None
#Group per user

counts = {}

for user, action in records:
  if user is None or action is None:
    continue
  if user not in counts:
    counts[user] = 0
  counts[user] += 1

print(counts)






#Task A — Loop + Conditionals ONLY (again)
#Problem
#Print values that are:
#not None
#greater than 0
#odd

values = [None, -5, 0, 1, 2, 3, 6, 7]

for v in values:
  if v is None:
    continue
  if v <= 0:
    continue
  if v % 2 == 0:
    continue 
  print(v)




#Dictionary Grouping (again)
#Problem
#Count how many valid events happened per day.

records = [
    ("2026-03-01", "click"),
    ("2026-03-01", "view"),
    ("2026-03-02", "click"),
    ("2026-03-02", None),
    (None, "click"),
    ("2026-03-01", "click"),
]

#Rules
#Ignore records where:
#day is None, or
#event is None
#Group per day

counts = {}

for day, event in records:
  if day is None or event is None:
    continue 
  if day not in counts:
    counts[day] = 0
  counts[day] += 1 

print(counts)
