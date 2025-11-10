# Demonstrate polymorphism using a function that behaves differently for objects of Circle and Rectangle classes. Use private variables to show data hiding.

import math

# Base class Shape 
class Shape:
    def area(self):
        pass  # abstract behavior — defined in subclasses


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius  # private variable (data hiding)

    # Method to calculate area
    def area(self):
        return math.pi * (self.__radius ** 2)

    # Method to display info
    def display(self):
        print(f"Circle with radius = {self.__radius}")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length    # private variable
        self.__width = width      # private variable

    # Method to calculate area
    def area(self):
        return self.__length * self.__width

    # Method to display info
    def display(self):
        print(f"Rectangle with length = {self.__length} and width = {self.__width}")


# Function demonstrating polymorphism
def show_area(shape_obj):
    # Same function behaves differently based on object type
    shape_obj.display()
    print(f"Area = {shape_obj.area():.2f}\n")


# Example usage
circle1 = Circle(5)
rectangle1 = Rectangle(4, 6)

# Demonstrating polymorphism
show_area(circle1)
show_area(rectangle1)
