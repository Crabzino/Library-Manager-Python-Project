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
                    element["Book ID"],
                    element.get("Borrow Time"),
                    element.get("Return Time")
                ))
            return books
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_books(books):
    with open("books.txt", "w") as book_data_to_write:
        book_data = [book.to_dict() for book in books]
        json.dump(book_data, book_data_to_write, indent=4)
        print("Books Saved Successfully")


def load_borrow_history():
    try:
        with open("borrow_history.json", "r") as history_file:
            return json.load(history_file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_borrow_history(history):
    with open("borrow_history.json", "w") as history_file:
        json.dump(history, history_file, indent=4)


def add_borrow_history(history, book_id, borrowed_at):
    book_id_str = str(book_id)
    if book_id_str not in history:
        history[book_id_str] = []

    history[book_id_str].append({
        "borrowed_at": borrowed_at,
        "returned_at": None
    })
    return history


def add_return_history(history, book_id, returned_at):
    book_id_str = str(book_id)
    if book_id_str not in history or not history[book_id_str]:
        history[book_id_str] = [{"borrowed_at": None, "returned_at": returned_at}]
    else:
        history[book_id_str][-1]["returned_at"] = returned_at

    return history


# version2