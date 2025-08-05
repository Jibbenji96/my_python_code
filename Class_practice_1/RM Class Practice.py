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