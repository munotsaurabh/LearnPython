"""
- Sets do not maintain insertion order.
- Duplicates are not allowed in Set. However, no error is given if user tries to add a duplicate element.
"""

cricket_players = {"Virat", "Rohit"}
hockey_players = {"Sunil", "Mandeep"}

cricket_players.add("Bhuvi")
print(cricket_players)

cricket_players.add("Rohit") # adding a duplicate element. 
print(cricket_players) # No error but duplicate element is not added.

hockey_players.remove("Sunil") # remove a set element
print(hockey_players)