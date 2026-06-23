class Book:
    def __init__(self, title, author, year, is_borrowed, book_id, borrow_time=None, return_time=None):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed
        self.book_id = book_id
        self.borrow_time = borrow_time
        self.return_time = return_time

    def mark_borrowed(self, borrowed_at):
        self.is_borrowed = "Yes"
        self.borrow_time = borrowed_at
        self.return_time = None
        print("Updated Successfully")

    def mark_returned(self, returned_at):
        self.is_borrowed = "No"
        self.return_time = returned_at
        print("Updated Successfully")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Release Year: {self.year}")
        print(f"Is Borrowed: {self.is_borrowed}")
        print(f"Book ID: {self.book_id}")
        print(f"Borrow Time: {self.borrow_time or 'Not borrowed yet'}")
        print(f"Return Time: {self.return_time or 'Not returned yet'}")

    def to_dict(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "Release Year": self.year,
            "Is Borrowed": self.is_borrowed,
            "Book ID": self.book_id,
            "Borrow Time": self.borrow_time,
            "Return Time": self.return_time
        }


# version2