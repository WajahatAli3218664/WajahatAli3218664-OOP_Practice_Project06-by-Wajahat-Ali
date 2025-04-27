#Using self
# Assignment 01:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name: str, marks: float) -> None:
        """Initialize the student with name and marks."""
        self.name = name
        self.marks = marks

    def display(self) -> None:
        """Display the student's details."""
        print(f"Student Name : {self.name}")
        print(f"Student Marks: {self.marks}")

def main():
    # Creating a student object
    student1 = Student(name="Wajahat", marks=85)
    
    # Displaying student details
    student1.display()

if __name__ == "__main__":
    main()
