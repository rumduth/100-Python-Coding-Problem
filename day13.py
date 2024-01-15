#Day 13
#Question 47:
#Define a class named Circle which can be constructed by a radius.
#The Circle class has a method which can compute the area.

import math
class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

#Question 48:
#Define a class named Rectangle which can be constructed by a length and width.
#The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return f'Area: {self.width * self.height}'


#Question 49:
#Define a class named Shape and its subclass Square. The Square class has an init
#function which takes a length as argument. Both classes have a area function which
#can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length
    def area(self):    
        return self.length * self.length

#Question 50:
#Please raise a RuntimeError exception.
def func50():
   raise RuntimeError('Something Wrong')
    
