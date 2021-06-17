friends = ["Virat", "Rohot", "Bhuvi", "Ashwin"]
scores = [3, 5, 12, 14]

zipped_dict = dict(zip(friends, scores))   # Zip two collections and convert into a dictionary
zipped_list = list(zip(friends, scores))   # Zip two collections and convert into a list

print (zipped_dict) 
print (zipped_list)