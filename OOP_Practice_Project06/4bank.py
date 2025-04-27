#Class Variables and Class Methods
#Assignment04:

#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances

class Bank:
    bank_name = "National Bank"  # Class variable shared across all instances

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        """
        Class method to change the bank name for all instances.
        """
        cls.bank_name = new_name

    def display_bank_name(self) -> None:
        """
        Instance method to display the current bank name.
        """
        print(f"Bank Name: {self.bank_name}")

def main():
    # Creating instances
    customer1 = Bank()
    customer2 = Bank()

    # Display initial bank name
    customer1.display_bank_name()

    # Changing the bank name using class method
    Bank.change_bank_name("Habib Bank")

    # Display updated bank name from another instance
    customer2.display_bank_name()

if __name__ == "__main__":
    main()
