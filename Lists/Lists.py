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

########################################
"""
Joining a list example
"""
friends = ["Mark", "Sam", "John"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")

########################################
players = ["Lionel", "Cristiano", "Paul", "Kylian", "Eden"]
numbers = [10, 7, 11, 9, 1]
players_new = ["Lionel", "Cristiano", "Paul", "Paul", "Kylian", "Eden"]

players.append("Luka")
print(players)

players.insert(2, "Vinicius")
print(players)

numbers.remove(9)
print(numbers)

numbers.pop()
print(numbers)

print(players.index("Kylian"))

print(players_new.count("Paul"))

players.sort()
print(players)

numbers.sort()
print(numbers)

players.reverse()
print(players)

players2 = players.copy()
print(players2)


players.extend(numbers)
print(players)

numbers.clear()
print(numbers)