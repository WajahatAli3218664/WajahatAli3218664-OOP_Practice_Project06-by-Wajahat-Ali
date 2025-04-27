#callable() and __call__()
#Assignment 19:
#Create a class Multiplier with an init() to set a factor. Define a call() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    """
    A class that multiplies an input by a predefined factor.
    
    Attributes:
        factor (int or float): The factor by which the input will be multiplied.
    """

    def __init__(self, factor: float) -> None:
        """
        Initializes the Multiplier with a given factor.

        Args:
            factor (float): The factor to multiply inputs with.
        """
        self.factor = factor

    def __call__(self, number: float) -> float:
        """
        Multiplies the given number by the factor.

        Args:
            number (float): The number to be multiplied by the factor.

        Returns:
            float: The result of the multiplication.
        """
        return self.factor * number


# 🚀 Example usage
if __name__ == "__main__":
    # Create an instance of Multiplier with factor 5
    multiplier = Multiplier(5)

    # Test if the object is callable using the callable() function
    print(f"Is the object callable? {callable(multiplier)}")  # Expected: True

    # Calling the object as a function
    result = multiplier(10)
    print(f"Multiplying 10 by factor 5 gives: {result}")  # Expected: 50

    # Additional test cases
    print(f"Multiplying 20 by factor 5 gives: {multiplier(20)}")  # Expected: 100
    print(f"Multiplying 7.5 by factor 5 gives: {multiplier(7.5)}")  # Expected: 37.5
