
# Mad Libs Game 🚀

print("Let's play Mad Libs!")

# Asking the user for inputs
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb (past tense): ")
place = input("Enter a place: ")

# Creating the story using the inputs
story = f"""
Today I went to the zoo and saw a(n) {adjective} {animal} jumping up and down in its tree.
It {verb} through the large tunnel that led to its {adjective} {place}.
It was the best day ever!
"""

# Printing the final story
print("\nHere's your Mad Libs story:")
print(story)
