
# GROUP MEMBERS:
# Nabiryo Miriam,
# Enock,
# Ashraf 
# and Terry


class Author:
    def __init__(self, name, birthdate, nationality):
     self.name = name
     self.birthdate = birthdate
     self.nationality = nationality

class Book:
    def __init__(self, title, author, isbn, pages,available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_info(self):
        return f"{self.title} by {self.author} Isbn: {self.isbn} Pages: {self.pages} Available: {self.available}"
    

    def checkout(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been checked out.")
        else:
            return False


class Fiction(Book):
    def __init__(self, title, author, isbn, pages, genre,available = True):
        super().__init__(title, author, isbn, pages,available)
        self.genre = genre

    def get_info(self):
        return f"{super().get_info()} Genre: {self.genre}"

class NonFiction(Book):
    def __init__(self, title, author, isbn, pages, topic):
        super().__init__(title, author, isbn, pages)
        self.topic = topic

    def get_info(self):
        return f"{super().get_info()} Topic: {self.topic}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]


    def search_by_author(self, author_name):
        return [book for book in self.books if author_name.lower() in book.author.name.lower()]

    def search_by_isbn(self, isbn):
        return [book for book in self.books if isbn == book.isbn]

    def display_inventory(self):
        print("Library inventory:")
        for book in self.books:
            status = "Available" if book.available else "Checked out"
            print(f"{book}, {status}")
#instancing our object
book1 = Fiction("Harry Porter","Mary Parker. T","098874564",500,"Magic")
book2 =NonFiction("Aminata","Charles Dickens","24356577",700,"Culter")
lib = Library()
#adding books
lib.add_book(book1)
lib.add_book(book2)
#displaying all books
lib.display_inventory()
#book1.checkout()













