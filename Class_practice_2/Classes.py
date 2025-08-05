# Exercise 1: Recipe Class
# Create a class called Recipe that has the following attributes:

# name
# ingredients (a list of ingredients)
# instructions
# Add methods to:

# add_ingredient(ingredient): Add an ingredient to the recipe.
# display_recipe(): Print out the recipe in a readable format.
# Instantiate a Recipe object and test your methods.

# Exercise 2: Music Album Class
# Create a class called Album that has the following attributes:

# title
# artist
# release_year
# songs (a list of song titles)
# Add methods to:

# add_song(song): Add a song to the album.
# remove_song(song): Remove a song from the album.
# list_songs(): Display all the songs in the album.
# Create an instance of the Album class and demonstrate the functionality of your methods.

# Exercise 3: Student Class
# Create a class called Student that has the following attributes:

# name
# grades (a list of grades)
# Add methods to:

# add_grade(grade): Add a grade to the student's list of grades.
# calculate_average(): Return the average of the grades.
# is_passing(): Return True if the average grade is 70 or above, otherwise return False.
# Instantiate a Student object and test the methods.

# Exercise 4: Bank Account Class
# Create a class called BankAccount with the following attributes:

# account_holder
# balance (initialized to 0)
# Add methods to:

# deposit(amount): Add an amount to the balance.
# withdraw(amount): Subtract an amount from the balance (ensure the balance doesn't go negative).
# display_balance(): Print the current balance.
# Create an instance of the BankAccount class and test the functionality.

# Exercise 5: Vehicle Class with Inheritance
# Create a base class called Vehicle with the following attributes:

# make
# model
# year
# Create a subclass called Car that adds an attribute:

# number_of_doors
# Add methods to both classes to:

# describe(): Return a description of the vehicle or car.
# Create instances of both Vehicle and Car, and call their describe() methods.

# Exercise 6: Library Management System
# Extend your previous Library class to include:

# A search_book(title) method that returns a list of books containing the provided title.
# Implement a method called borrow_book(book) which removes a book from the library and adds it to a borrowed list.

# Implement a method called return_book(book) which removes a book from the borrowed list and adds it back to the library.

# Test the new functionalities with various books.



class Recipe():

    def __init__(self, ingredients, instructions):
        self.ingredients = ingredients
        self.instructions = instructions
    
    def add_ingredient(self, new_ingredient):
        self.ingredients.append(new_ingredient)

    def display_recipe(self):
        return f"The ingredients you need are {', '.join(self.ingredients)}, and you must {self.instructions}"
    

# new_recipe = Recipe(["Cheese", "Tomato", "Basil"], "combine the ingredients")

# new_recipe.add_ingredient("Onion")

# print(new_recipe.display_recipe())

class Album():
    def __init__(self, title, artist, release_year, songs):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.songs = songs

    def add_song(self, new_song):
        self.songs.append(new_song)
    
    def remove_song(self, song):
        self.songs.remove(song)
    
    def list_songs(self):
        return ', '.join(self.songs)
    
# new_album = Album("MBDTF", "Kanye West", "2010", ["Monster", "Runaway"])

# new_album.add_song("Cheesin")

# print(new_album.list_songs())

# new_album.remove_song("Cheesin")

# print(new_album.list_songs())


class Student():

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def add_grade(self, new_grade):
        self.grades.append(new_grade)
    
    def calculate_average(self):
        return (sum(self.grades))/(len(self.grades))
    
    def is_passing(self):
        total_grade = self.calculate_average()
        return True if total_grade > 70 else False
    

# new_student = Student("Ben", [68, 54, 10, 35])

# print(new_student.is_passing())



class BankAccount():
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return f"Your new balance is {self.balance}"
    
    def withdraw(self, withdrawal_amount):
        if self.balance > withdrawal_amount:
            self.balance -= withdrawal_amount
            return f"Your new balance is {self.balance}"
        else:
            return f"{self.account_holder} does not have the facilities for that big man"
        
    def display_balance(self):
        print(self.balance)

# new_account = BankAccount("Ben")

# new_account.deposit(1000)
# new_account.display_balance()

# print(new_account.withdraw(100))


class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def describe(self):
        return f" This vehicle is a {self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def describe(self):
        parent_description =  super().describe() 
        return f"{parent_description} with {self.number_of_doors} doors"
    

# new_vehicle = Vehicle("Volve", "XC90", "2021")
# new_car = Car("Citroen", "C3", "2019", "4")

# print(new_vehicle.describe())
# print(new_car.describe())
