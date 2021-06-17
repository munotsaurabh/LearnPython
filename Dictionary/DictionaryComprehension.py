friends = ["Virat", "Rohot", "Bhuvi", "Ashwin"]
scores = [3, 5, 12, 14]

friends_scores = {            # Dictionary comprehension
  friends[i]:scores[i]
  for i in range(len(friends))
  if scores[i] > 10          # Comprehension with condition
}
print (friends_scores)