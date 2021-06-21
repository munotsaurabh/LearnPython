"""
- "__init__" is a reserved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

- The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
"""

class Rectangle:
    def __init__(self, length, breadth): 
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth


r = Rectangle(160, 120)
print("Area of Rectangle: %s sq units" % (r.calculate_area()))
