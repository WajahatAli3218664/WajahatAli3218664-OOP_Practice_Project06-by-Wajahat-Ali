# 📄 Abstract Classes and Methods

#Assignment 09:
#Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# 🔷 Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of a shape.
        Must be implemented by subclasses.
        """
        pass

# 🟥 Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize the rectangle with length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: Area of the rectangle.
        """
        return self.length * self.width

# 🚀 Example usage
if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    print(f"📐 The area of the rectangle is: {rectangle.area()} square units")
