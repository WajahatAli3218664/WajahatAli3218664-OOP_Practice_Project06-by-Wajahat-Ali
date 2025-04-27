#Make a Custom Class Iterable
#Assignment 21:
#Create a class Countdown that takes a start number. Implement iter() and next() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    """
    Countdown Class to iterate through numbers starting from the given number down to 0.
    
    This class implements both __iter__() and __next__() methods to make the Countdown object iterable.
    When used in a for loop, it will print each number in the countdown from start to 0.
    """
    
    def __init__(self, start: int):
        """
        Initializes the countdown sequence starting from the given number.
        
        Args:
            start (int): The starting number for the countdown.
        """
        self.start = start

    def __iter__(self):
        """
        Returns the iterator object itself for use in a for-loop.
        """
        return self

    def __next__(self):
        """
        Returns the next number in the countdown.
        If the countdown is finished (start < 0), raises StopIteration.
        
        Returns:
            int: The current countdown number.
        
        Raises:
            StopIteration: When the countdown is finished.
        """
        if self.start < 0:
            raise StopIteration  # 🛑 Stop the iteration when countdown ends
        current = self.start
        self.start -= 1  # ⏬ Decrement the number after returning it
        return current

# 🚀 Example usage
if __name__ == "__main__":
    c = Countdown(5)  # 🔢 Start the countdown from 5
    print("Starting Countdown: 🚀")
    for number in c:
        print(f"{number} ⏳")  # Show the countdown with emoji for visual appeal
