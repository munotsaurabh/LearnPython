name = "Sam"
user_input = input("Enter your name: ") # input fn returns a string

print(f"Hello {name}. My name is {user_input}.")

####################

age = input("Enter your age: ")
print(f"You have lived for {age * 12} months.") #This will print the entered age 12 times repetitively because `age` variable holds string value

####################

age = input("Enter your age: ")
print(f"You have lived for {int(age) * 12} months.")

name= input("Enter your name: ")
print(f"Hello {name}!")

age= input("Enter your age: ")
print(f"Hey {name}. You are {age} years old.")