import math

class Shape:
    def __init__(self):
        pass
    
    def GetArea(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def GetArea(self):
        return math.pi * self.radius**2

class Rectangle(Shape):  
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def GetArea(self):
        return self.length * self.width