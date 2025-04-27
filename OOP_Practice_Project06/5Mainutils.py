#Static Variables and Static Methods
#Assignment 05:

#Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used



class MathUtils:
    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method to return the sum of two numbers.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: Sum of a and b.
        """
        return a + b

def main():
    # Example usage of the static method
    result = MathUtils.add(5, 10)
    print(f"The sum is: {result}")

if __name__ == "__main__":
    main()
