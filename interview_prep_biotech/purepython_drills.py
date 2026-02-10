#Given a list of numbers, print only even, positive numbers.
# numbers = [2, -1, 4, 0, None, 7, 8]

for n in numbers:
    if n is None:
      continue 
    if n < 0:
      continue 
    if n % 2 != 0: #If dividing this number by 2 leaves something left over (remainder), skip it.
      continue
    print(n)


#Mini Exercise Set — Loops + Conditionals
#Exercise 1 (very easy, warm-up)

#Problem:
#Print only non-null values from the list.

#values = [1, None, 3, None, 5]

#Rules
#Use a for loop
#Use if
#Use continue when appropriate

for v in values: 
    if v is None:
      continue
    print(v)


#Exercise 2
#Problem reminder:
#Print numbers that are greater than 5.
#numbers = [2, 7, 1, 9, 5, 10]

 # continue = you want to filter out unwanted values early (if it's x then continue skips it)

for n in numbers:
    if n > 5:
    print(n)


#Exercise 3 again, now that continue is clearer:
#Print values that are:
#not None
#greater than 0
#odd
#nums = [None, -3, 0, 2, 3, 5, 8, 9]

for n in nums:
    if n is None:
      continue
    if n <= 0:
      continue 
    if n % 2 == 0:
      continue
    print(n)



