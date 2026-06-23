from library import Book
from file_manager import save_books, load_books

books = load_books()


welcome_message = """
                                    ==============================
                                    Welcome to the Library Manager
                                    ==============================
"""
menu_options = """
                                        1. View All Books
                                        2. Add Book
                                        3. Search Book(By ID)
                                        4. Remove Book(By ID)
                                        5. Borrow Book(By ID)
                                        6. Return Book(BY ID)
                                        7. Save
                                        8. Exit
"""


def view_all_books():
    if not books:
        print("No Students Found")
    else:
        for book in books:
            book.display_info()
            print("-" * 30)



def add_book():
    user_answer1 = input("To add a book, the system requires you to have the following: Title, Author, Release Year, Is Borrowed Status. Do you have the following?").lower()
    if user_answer1 == "yes":
        user_title = input("Enter Book Title: ").title()
        user_author = input("Enter Author: ").title()
        user_release = input("Enter release year: ")
        user_borrowed = input("Enter Borrow Status(Yes/No): ").title()
        user_id = int(input("Create a 6 digit ID for the book: "))
        books.append(Book(user_title, user_author, user_release, user_borrowed, user_id))
        print("Book Added Successfully")



def search_book():
    try:
        user_answer2 = int(input("Enter the book you would like to search for via 6 digit ID: "))
        for book in books:
            if book.book_id == user_answer2:
                book.display_info()
                return
        print("Book Not found")
    except ValueError:
        print("Enter a valid 6 digit ID")



def remove_book():
    try:
        user_answer3 = int(input("Enter the 6 digit ID of the book you would like to remove: "))
        for book in books:
            if book.book_id == user_answer3:
                books.remove(book)
                print("Book removed succesfully")
                return
        print("Book Not Found")
    except ValueError:
        print("Enter a valid 6 digit ID")
       


def borrow_book():
    user_answer4 = int(input("Enter the 6 digit ID of the book you would like to borrow: "))
    confirmation = input("Are you sure you would like to borrow the book? ").lower()
    if confirmation == "yes":
        for book in books:
            if book.book_id == user_answer4:
                book.update_is_borrowed(user_answer4, confirmation.title())
                return
   


def return_book():
    user_answer5 = int(input("Enter the 6 digit ID of the book you would like to return: "))
    confirmation2 = input("Are you sure you would like to return this book now?").lower()
    if confirmation2 == "yes":
        for book in books:
            if book.book_id == user_answer5:
                book.update_is_borrowed(user_answer5, "No") 
                return




def save_program():
    save_books(books)



def exit_program():
    print("Goodbye")
    exit()





if __name__ == "__main__":
    print(f"{welcome_message}")
    print(f"{menu_options}")
    while  True:
        me = int(input("Choose an option: "))
        if me == 1:
            view_all_books()
        elif me == 2:
            add_book()
        elif me == 3:
            search_book()
        elif me == 4:
            remove_book()
        elif me == 5:
            borrow_book()
        elif me == 7:
            save_program()
        elif me == 8:
            exit_program()
        elif me == 6:
            return_book()
        else:
            print("Invalid Option")
