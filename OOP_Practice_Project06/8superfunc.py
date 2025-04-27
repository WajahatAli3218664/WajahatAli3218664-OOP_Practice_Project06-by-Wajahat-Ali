#The super() Function
#Assignment 08:

#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor

class Person:
    def __init__(self, name):
        """
        Constructor for Person class.
        
        Args:
            name (str): Name of the person.
        """
        self.name = name

    def display_name(self):
        """
        Display the name of the person.
        """
        print(f"Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        """
        Constructor for Teacher class.
        Calls the base class constructor using super().
        
        Args:
            name (str): Name of the teacher.
            subject (str): Subject taught by the teacher.
        """
        super().__init__(name)  # Calling the parent class constructor
        self.subject = subject

    def display_teacher_info(self):
        """
        Display teacher's full information.
        """
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
if __name__ == "__main__":
    teacher = Teacher("Mr. Khan", "Math")
    teacher.display_teacher_info()
