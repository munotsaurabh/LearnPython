friend_ages = {"Sam": 30, "Virat": 29, "Rohit": 31}

print(friend_ages["Virat"]) #printing the value of the key Virat

friend_ages ["Bhuvi"] = 28 # adding a new dict element
friend_ages ["Rohit"] = 33 # updating the value of existing element

print(friend_ages)

########################################

friends = (                     # tuple of dictionaries
  {"name": "Mark", "age": 34},
  {"name": "Steve", "age": 33},
  {"name": "Keith", "age": 31}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

########################################
"""
dict function turns data into a dictionary
"""
friends = [("Ken", 24), ("Neil", 20), ("Mini", 21)] # list of tuples
friends_ages = dict(friends) # dict function to convert friends list to dictionary
print (friends_ages)