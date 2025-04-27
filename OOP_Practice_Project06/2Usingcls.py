#Using cls
#Assignment 02:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    _count: int = 0  # Class variable (protected)

    def __init__(self) -> None:
        """Increment the object counter upon each new instance creation."""
        Counter._count += 1

    @classmethod
    def display_count(cls) -> None:
        """Display the total number of objects created."""
        print(f"Total objects created: {cls._count}")

    @classmethod
    def reset_count(cls) -> None:
        """Reset the object count to zero."""
        cls._count = 0
        print("Counter has been reset to 0.")

def main():
    # Creating multiple Counter objects
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()

    # Displaying the current count
    Counter.display_count()

    # Resetting the counter
    Counter.reset_count()

    # Displaying count after reset
    Counter.display_count()

if __name__ == "__main__":
    main()

