#Class Decorators

#Assignment 17 :
#Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    """
    🛠️ Class decorator to add a greet() method.
    
    Adds a method `greet` to the class that returns
    'Hello from Decorator!'.
    
    Args:
        cls (class): The class to modify.
        
    Returns:
        class: The modified class with greet() method.
    """
    def greet(self):
        return "👋 Hello from Decorator!"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    """
    🧑 A simple class representing a person.
    
    Attributes:
        name (str): Name of the person.
    """
    def __init__(self, name):
        self.name = name

# 🚀 Example usage
if __name__ == "__main__":
    p = Person("Aisha")
    print(p.greet())  # Output: 👋 Hello from Decorator!
