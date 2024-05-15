import lib_db


class Book:
    def __init__(self, ISBN, Title, Author, Price, Pages):
        self.ISBN = ISBN
        self.Title = Title
        self.Author = Author
        self.Price = Price
        self.Pages = Pages
        lib_db.insert(self.ISBN, self.Title, self.Author, self.Price, self.Pages)


def add(ISBN, Title, Author, Price, Pages):
    book = Book(ISBN, Title, Author, Price, Pages)


def delete(ISBN):
    lib_db.delete(ISBN)


def list_book(self):
    pass


def search(ISBN):
    return lib_db.find(ISBN)
