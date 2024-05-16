import lib_db


class Book:
    def __init__(self, ISBN, Title, Author, Price, Pages):
        self.ISBN = ISBN
        self.Title = Title
        self.Author = Author
        self.Price = Price
        self.Pages = Pages
        lib_db.insert(self.ISBN, self.Title, self.Author, self.Price, self.Pages)

    @staticmethod
    def delete(ISBN):
        lib_db.delete(ISBN)

    @staticmethod
    def list_book():
        return lib_db.all()

    @staticmethod
    def search(ISBN):
        return lib_db.find(ISBN)

    @staticmethod
    def all():
        return lib_db.all()


