#Access Modifiers: Public, Private, and Protected
#Assignment 07:

#Create a class Employee with:

#a public variable name,

#a protected variable _salary, and

#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.



class Employee:
    def __init__(self, name, salary, ssn):
        """
        Constructor to initialize employee details.
        """
        self.name = name          # Public attribute
        self._salary = salary     # Protected attribute
        self.__ssn = ssn           # Private attribute

    def display_info(self):
        """
        Display employee information (except private data).
        """
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")

    def get_ssn(self):
        """
        Public method to safely access the private SSN.
        """
        return self.__ssn

def main():
    # Creating an Employee object
    emp = Employee("Sara", 50000, "123-45-6789")
    
    # Accessing public variable
    print("Accessing Public Variable:")
    print(emp.name)  # ✅ Public - directly accessible
    
    # Accessing protected variable
    print("\nAccessing Protected Variable:")
    print(emp._salary)  # ⚠️ Protected - accessible but should be accessed within subclass or class only

    # Accessing private variable directly (will cause error if uncommented)
    # print(emp.__ssn)  # ❌ Private - Not directly accessible (will throw AttributeError)

    # Accessing private variable using name mangling
    print("\nAccessing Private Variable using Name Mangling:")
    print(emp._Employee__ssn)  # ✅ Correct way if really necessary

    # OR accessing private variable safely through a method
    print("\nAccessing Private Variable using Getter Method:")
    print(emp.get_ssn())  # ✅ Recommended way

if __name__ == "__main__":
    main()
