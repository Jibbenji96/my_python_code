# Exercise 1: Basic Class Definition
# Create a class called Book that has the following attributes:

# title
# author
# published_year
# Add a method called describe() that returns a string describing the book in the following format:

# "Title: [title], Author: [author], Published Year: [year]"
# Instantiate a Book object and call the describe() method to see the output.

# Exercise 2: Adding Methods
# Extend the Book class by adding a method called is_classic(). This method should return True if the book was published more than 50 years ago, and False otherwise.

# Test the is_classic() method with several instances of Book, using different published years.

# Exercise 3: Inheritance
# Create a new class called EBook that inherits from the Book class. Add an additional attribute called file_size to represent the size of the eBook.

# Override the describe() method in the EBook class to include the file size in the output.

# Create an instance of EBook and call the describe() method to verify that it works correctly.

# Exercise 4: Class Variables
# Modify the Book class to include a class variable called book_count that keeps track of the number of Book instances created.

# Increment book_count in the __init__ method each time a new Book is instantiated.

# Create multiple Book instances and print the value of Book.book_count to verify that it accurately reflects the number of books created.

# Exercise 5: Class Methods
# Add a class method called from_string(cls, book_string) in the Book class. This method should take a string in the format "Title, Author, Year" and return an instance of Book created from that string.

# Test the from_string() method by creating a Book instance from a string.

# Exercise 6: Composition
# Create a class called Library that contains a list of Book objects.

# Include methods in Library to:

# Add a book to the library.
# Remove a book from the library.
# Display a list of all books in the library.
# Instantiate the Library class and test its functionality by adding and removing books.

import datetime

class Book():
    book_count = 0

    def __init__(self, title, author, published_year):
        
        self.title = title
        self.author = author
        self.published_year = published_year
        Book.book_count += 1

    @classmethod
    def from_string(cls, book_string):
        split_book =book_string.split(", ")
        
        book_instance = cls(split_book[0], split_book[1], split_book[2])

        return book_instance 

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}, Published Year: {self.published_year}"
    
    def is_classic(self):
        current_date = datetime.datetime.now().year
        if current_date - int(self.published_year) > 50:
            return True
        else:
            return False
        
class EBook(Book):
    def __init__(self, title, author, published_year, file_size):
        super().__init__(title, author, published_year)
        self.file_size = file_size
    
    def describe(self):
        return f"Title: {self.title}, Author: {self.author}, Published Year: {self.published_year}, File Size: {self.file_size}"

class Library():
    def __init__(self):
        self.library = []

    def add_book_to_library(self, book):
        self.library.append(book)

    def remove_book_from_library(self, book):
        self.library.remove(book)

    def list_library(self):
        print(self.library)
        
new_library = Library()

new_library.add_book_to_library("Peak Limestone")
new_library.add_book_to_library("Peak Bouldering")
new_library.add_book_to_library("Trad Climbing")


new_library.list_library()


book_string = "On the Road, Jack Kerouac, 1957" 
my_book = Book.from_string(book_string)
print(my_book.describe())


On_the_road = Book("On the Road", "Jack Kerouac", "1957")
Bible = Book("The Bible", "Jesus","0")

print(Book.book_count)
