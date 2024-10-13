import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by derived classes")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width  # Return numerical value only

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius     

    def area(self):
        return math.pi * (self.radius ** 2)  # Return numerical value only

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")  # Format output here

if __name__ == "__main__":
    main()
