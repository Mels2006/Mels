# Write an abstract class with name GeometricFigure
# Write 2 geometric figure classes by inheriting from GeometricFigure
# Write 2 functions
# get_perimeter -> return perimeter of figure
# get_area -> return area of figure
from abc import ABC, abstractmethod
import math
class GeometricFigure(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass
    @abstractmethod
    def get_area(self):
        pass
class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius**2

class Rectangle(GeometricFigure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle:")
print(f"Perimeter: {circle.get_perimeter()}")
print(f"Area: {circle.get_area()}")

print("Rectangle:")
print(f"Perimeter: {rectangle.get_perimeter()}")
print(f"Area: {rectangle.get_area()}")


    