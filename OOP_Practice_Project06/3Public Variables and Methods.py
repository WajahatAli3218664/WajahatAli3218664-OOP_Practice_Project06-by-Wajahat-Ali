#Public Variables and Methods
#Assignment03:

#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class

class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        """Initialize the Car object with brand, model, and year."""
        self.brand = brand        # Public variable
        self.model = model        # Public variable
        self.year = year          # Public variable

    def start(self) -> None:
        """Public method to simulate starting the car."""
        print(f"{self.brand} {self.model} ({self.year}) has started.")

    def display_info(self) -> None:
        """Public method to display car details."""
        print(f"Car Info: {self.year} {self.brand} {self.model}")

def main():
    # Instantiating the Car class
    car1 = Car(brand="Toyota", model="Corolla", year=2023)
    car2 = Car(brand="Honda", model="Civic", year=2022)

    # Accessing public variables
    print(car1.brand)
    print(car2.model)

    # Accessing public methods
    car1.start()
    car2.start()

    car1.display_info()
    car2.display_info()

if __name__ == "__main__":
    main()
