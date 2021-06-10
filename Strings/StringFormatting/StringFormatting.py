age = 30
print(f"You are {age}") #f String example

############################

name = "Sam"
greeting = "How are you, {}?"
final_greeting = greeting.format(name)
print(final_greeting) 

name= "Bob"
new_greeting = greeting.format(name)
print(new_greeting) #format function example

############################

person_name = "John"
greeting = "Hello there, {arg_name}"
john_greeting = greeting.format(arg_name=person_name)
print(john_greeting) #another format function example
