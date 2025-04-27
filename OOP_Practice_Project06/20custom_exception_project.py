#Creating a Custom Exception
#Assignment 20:
#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    """
    Custom exception to handle invalid age input.
    
    This exception is raised when the age provided is below 18.
    """
    def __init__(self, message: str = "Age must be 18 or above."):
        self.message = message
        super().__init__(self.message)

def check_age(age: int) -> None:
    """
    Function to check if the provided age is valid (18 or above).
    
    Args:
        age (int): The age to be checked.

    Raises:
        InvalidAgeError: If the age is less than 18.
    """
    if age < 18:
        raise InvalidAgeError(f"Provided age {age} is below 18.")
    else:
        print(f"Age {age} is valid.")

# 🚀 Example usage
if __name__ == "__main__":
    # Test Case 1: Age less than 18 (invalid)
    try:
        check_age(16)  # Invalid age test
    except InvalidAgeError as e:
        print(f"Error: {e}")

    # Test Case 2: Age equal to 18 (valid)
    try:
        check_age(18)  # Valid age test
    except InvalidAgeError as e:
        print(f"Error: {e}")

    # Test Case 3: Age above 18 (valid)
    try:
        check_age(25)  # Valid age test
    except InvalidAgeError as e:
        print(f"Error: {e}")

