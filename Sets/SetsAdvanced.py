cricket_players = {"Virat", "Rohit", "Bhuvi"}
hockey_palyers = {"Rohit", "Mandeep"}

cricket_but_not_hockey= cricket_players.difference(hockey_palyers) #elements in cricket but not in hockey
print (cricket_but_not_hockey) 

hockey_but_not_cricket = hockey_palyers.difference(cricket_players) #elements in hockey but not in cricket
print(hockey_but_not_cricket) 

cricket_players = {"Virat", "Rohit", "Bhuvi"}
hockey_palyers = {"Rohit", "Mandeep"}

not_in_both = cricket_players.symmetric_difference(hockey_palyers) #elements not in both
print(not_in_both) 

common = cricket_players.intersection(hockey_palyers) #common elements in both sets
print(common)

without_duplicates = hockey_palyers.union(cricket_players) #unites both sets removing duplicates
print (without_duplicates)