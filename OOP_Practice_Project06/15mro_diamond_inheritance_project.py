#Method Resolution Order (MRO) and Diamond Inheritance
#Assignment 15:

#Create four classes:
#A with a method show(),
#B and C that inherit from A and override show(),
#D that inherits from both B and C.
#Create an object of D and call show() to observe MRO.

class A:
    """
    🧱 Base class A with a show() method.
    """

    def show(self):
        """
        Display class name.
        """
        print("🧱 Class A")

class B(A):
    """
    🏗️ Class B inherits from A and overrides show().
    """

    def show(self):
        """
        Display class name.
        """
        print("🏗️ Class B")

class C(A):
    """
    🏗️ Class C inherits from A and overrides show().
    """

    def show(self):
        """
        Display class name.
        """
        print("🏗️ Class C")

class D(B, C):
    """
    🏢 Class D inherits from B and C (Diamond Inheritance).
    """
    pass

# 🚀 Example Usage
if __name__ == "__main__":
    # Create object of class D
    d = D()
    
    # Call show() method
    d.show()
    
    # Print Method Resolution Order
    print("\n🔎 MRO (Method Resolution Order) for Class D:")
    for cls in D.__mro__:
        print(f"➡️ {cls.__name__}")

