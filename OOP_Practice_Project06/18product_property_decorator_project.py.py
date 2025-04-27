#Property Decorators: @property, @setter, and @deleter
#Assignment 18:

#Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.son.


class Product:
    """
    🛒 Class representing a product with a price.

    Attributes:
        _price (float): The private price of the product.
    """

    def __init__(self, price):
        """
        Initializes the Product with a given price.

        Args:
            price (float): The initial price of the product.
        """
        self._price = price

    @property
    def price(self):
        """
        Getter for the product price.

        Returns:
            float: Current price of the product.
        """
        print("🔎 Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        """
        Setter for the product price.

        Args:
            value (float): New price to set.
        """
        if value < 0:
            raise ValueError("🚫 Price cannot be negative.")
        print(f"✏️ Updating the price to {value}...")
        self._price = value

    @price.deleter
    def price(self):
        """
        Deleter for the product price.
        """
        print("🗑️ Deleting the price...")
        del self._price


# 🚀 Example usage
if __name__ == "__main__":
    p = Product(100)

    # Accessing price
    print(p.price)  # Output: 100

    # Updating price
    p.price = 200
    print(p.price)  # Output: 200

    # Deleting price
    del p.price
