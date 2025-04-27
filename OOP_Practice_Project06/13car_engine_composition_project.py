 #Composition
#Assignment 13:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    """
    🛠️ Engine class to simulate engine operations.
    """

    def start(self):
        """
        🚗 Start the engine.
        """
        print("🛞 Engine started and running smoothly.")

class Car:
    """
    🚘 Car class composed with an Engine object.
    """

    def __init__(self, engine):
        """
        Initialize the Car with an Engine.

        Args:
            engine (Engine): An instance of the Engine class.
        """
        self.engine = engine

    def start_car(self):
        """
        🚗 Start the car by starting its engine.
        """
        print("🔑 Starting the car...")
        self.engine.start()

# 🚀 Example usage
if __name__ == "__main__":
    engine = Engine()
    car = Car(engine)
    car.start_car()
