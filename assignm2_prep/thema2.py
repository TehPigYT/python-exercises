import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def print_areas(shapes):
    for shape in shapes:
        print(shape.area())

shapes = [
    Circle(5),
    Rectangle(4, 5),
    Circle(2),
    Rectangle(7, 3)
]

print_areas(shapes)