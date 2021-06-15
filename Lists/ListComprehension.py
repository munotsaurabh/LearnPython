scores = [0, 1, 2, 3, 4]

doubled_scores = [score * 2 for score in scores] 
print(doubled_scores)

modified_scores = [10 for score in scores]
print (modified_scores)

friend_score = [f"My friend has a score of {score}" for score in scores]
print (friend_score)

names = ["Virat", "Rohit", "Bhuvi"]
lower = [name.lower() for name in names]
print (lower)


friends = ["Virat", "rohit", "bhuvi", "Jaddu"]
guests = ["ishant", "ajinkya", "virat", "jaddu", "Ashwin"]

friends_lower= [f.lower() for f in friends]

invited_friends = [name.title()              # Comprehension with condition 
for name in guests 
if name.lower() in friends_lower
]

print (invited_friends)