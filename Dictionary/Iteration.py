friends_ages = {"Virat": 32, "Rohit":33, "Bhuvi":30, "Jaddu":31}

for friend in friends_ages:  # Prints the keys
  print (friend)

for age in friends_ages.values():  # Prints values
  print (age)

for name, age in friends_ages.items(): # Iterating over each item in dictionary
  print(f"{name} is {age} years old")