class Book:
    def __init__ (self, title, author, year, is_borrowed, book_id):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed
        self.book_id = book_id


    def update_is_borrowed(self, id_for_book, update_for_is_borrowed):
        if id_for_book == self.book_id:
            self.is_borrowed = update_for_is_borrowed
            print("Updated Successfully")
        else:
            print("Book Not Found")


    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Release Year: {self.year}")
        print(f"Is Borrowed: {self.is_borrowed}")
        print(f"Book ID: {self.book_id}")

    
    def to_dict(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "Release Year": self.year,
            "Is Borrowed": self.is_borrowed,
            "Book ID": self.book_id
        }


#version1