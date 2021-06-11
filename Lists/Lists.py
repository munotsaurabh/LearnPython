friends = ["Mark", "Sam", "John"]
print (friends[0])

########################################

list_in_list = [
  ["Virat", 24], 
  ["Hardik", 20], 
  ["Bhuvi", 30]
  ]
print (list_in_list[1]) #Prints the entire second element of the outer list i.e. ['Sam', 20]
print (list_in_list[0][0]) # Prints first element of the inner list

########################################
"""
Add and remove from a list
"""
list_in_list.append(["Rohit", 32])
print (list_in_list)

friends.remove("Sam")
print (friends)

list_in_list.remove (["Hardik", 20])
print (list_in_list)