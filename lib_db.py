import sqlite3


def create():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books_table(ISBN INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Price FLOAT, Pages INTEGER)")


def insert(ISBN, Title, Author, Price, Pages):
    create()
    try:
        cursor.execute("INSERT INTO books_table VALUES(?,?,?,?,?)", [ISBN, Title, Author, Price, Pages])
        print("book has been saved successfully")
    except(sqlite3.IntegrityError):
        raise ValueError("ISBN must be a unique number")
    database.commit()


def find(ISBN):
    book = cursor.execute("SELECT * FROM books_table where ISBN= ?", [ISBN]).fetchone()
    if book == None:
        return "car not found"
    return book


def delete(ISBN):
    cursor.execute("DELETE FROM books_table WHERE ISBN = ?", [ISBN])
    database.commit()


def all():
    books = cursor.execute("SELECT * FROM books_table")
    return books


database = sqlite3.connect("../library/lib_database.db")

cursor = database.cursor()
