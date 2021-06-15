"""
enumerate() function assigns a number to each element in the list
"""

friends = ["Virat", "Rohit", "Bhuvi", "Ashwin"]

enumerate_list = list(enumerate(friends))
enumerate_dict = dict(enumerate(friends, start=101)) # 'start' argument for assigning a number for each element in the list

print (enumerate_list)
print (enumerate_dict)