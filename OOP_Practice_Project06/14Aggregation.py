#Aggregation
#Assignment14:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    """
    👨‍💼 Employee class represents an employee with a name.
    """

    def __init__(self, name):
        """
        Initialize the Employee.

        Args:
            name (str): Name of the employee.
        """
        self.name = name

    def get_details(self):
        """
        Get the employee details.

        Returns:
            str: Formatted employee name.
        """
        return f"Employee Name: {self.name}"

class Department:
    """
    🏢 Department class aggregates an Employee instance.
    """

    def __init__(self, department_name, employee):
        """
        Initialize the Department with an employee.

        Args:
            department_name (str): Name of the department.
            employee (Employee): An instance of the Employee class.
        """
        self.department_name = department_name
        self.employee = employee

    def display_info(self):
        """
        Display department and associated employee details.
        """
        print(f"🏢 Department: {self.department_name}")
        print(f"👨‍💼 {self.employee.get_details()}")

# 🚀 Example usage
if __name__ == "__main__":
    emp1 = Employee("Hamza")
    department = Department("IT Department", emp1)
    department.display_info()
