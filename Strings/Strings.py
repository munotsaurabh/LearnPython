"""
This is a String example file. Python treats this like a comment.
"""

single_quote_string = 'Hello world.'
double_quote_string = "Hey, it's me"
string_with_escaping = "She said \"You are beautiful\""
name= "Sam"
greetings = "Hello, " +name
multiline_string = """
Hey there.
Welcome to the show
"""
to_lower = "HELLO WORLD"

print (single_quote_string)
print (double_quote_string)
print (multiline_string)
print(greetings)
print(string_with_escaping)
print ("Just to check git repo configured")
print ("Hello\nWorld")
print (to_lower.lower())
print (to_lower.lower().islower())
print(len(name))
print (name[0])
print(name.lower().index("s"))
print(name.replace("Sam", "Tom"))
print (name.replace("S", "M"))