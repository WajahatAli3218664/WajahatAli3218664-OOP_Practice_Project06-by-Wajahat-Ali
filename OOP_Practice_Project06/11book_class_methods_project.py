# 📄 Class Methods

#Assignment 11:
#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added

class Book:
    """
    📖 Book class to manage total number of books created.
    """

    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title, author):
        """
        Initialize a new Book instance.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
        """
        self.title = title
        self.author = author
        Book.total_books += 1  # Increment total_books when a new book is created

    @classmethod
    def display_total_books(cls):
        """
        📊 Display the total number of books created.
        """
        print(f"📚 Total books created so far: {cls.total_books}")

    def show_details(self):
        """
        📋 Display details of the book.
        """
        print(f"📖 Title: {self.title}\n✍️ Author: {self.author}")

# 🚀 Example usage
if __name__ == "__main__":
    # Creating book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    # Showing details
    print("📚 Book Collection:")
    book1.show_details()
    book2.show_details()
    book3.show_details()

    # Displaying total book count
    print("\n📈 Book Summary:")
    Book.display_total_books()
