#Constructors and Destructors
#Assignment 06:

#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).




class Logger:
    def __init__(self):
        """
        Constructor: Called when an object of Logger is created.
        """
        print("✅ Logger object created.")

    def __del__(self):
        """
        Destructor: Called when an object of Logger is destroyed.
        """
        print("🗑️ Logger object destroyed.")

def main():
    # Creating and destroying a Logger object
    logger = Logger()
    
    # Explicitly deleting the object
    del logger

if __name__ == "__main__":
    main()
