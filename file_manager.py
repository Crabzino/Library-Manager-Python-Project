import json
from library import Book

def load_books():
    try:
        with open("books.txt", "r") as book_data:
            data = json.load(book_data)
            books = []
            for element in data:
                books.append(Book(
                    element["Title"],
                    element["Author"],
                    element["Release Year"],
                    element["Is Borrowed"],
                    element["Book ID"]
                ))
            return books
    except FileNotFoundError:
            return []
    except json.JSONDecodeError:
            return []




def save_books(books):
    with open("books.txt", "w") as book_data_to_write:
        book_data = [book.to_dict() for book in books]
        json.dump(book_data, book_data_to_write, indent = 4)
        print("Books Saved Successfully")