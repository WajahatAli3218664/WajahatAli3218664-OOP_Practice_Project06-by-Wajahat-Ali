#Instance Methods
#Assignment 10:

#Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name

class Dog:
    """
    🐾 Dog class represents a dog with a name and breed.
    """

    def __init__(self, name, breed):
        """
        Initialize a Dog instance.

        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog.
        """
        self.name = name
        self.breed = breed

    def bark(self):
        """
        🗣️ Make the dog bark.
        """
        print(f"🐶 {self.name} the {self.breed} is barking! Woof! Woof!")

    def info(self):
        """
        📋 Display the dog's information.
        """
        print(f"📌 Name: {self.name}\n📌 Breed: {self.breed}")

# 🚀 Example usage
if __name__ == "__main__":
    # Creating dog instances
    dog1 = Dog("Tommy", "Bulldog")
    dog2 = Dog("Lucy", "Golden Retriever")

    # Displaying information
    print("🐕‍🦺 Dog Details:")
    dog1.info()
    dog2.info()

    # Dogs barking
    print("\n🔊 Barking Sounds:")
    dog1.bark()
    dog2.bark()
