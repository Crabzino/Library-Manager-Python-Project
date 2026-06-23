from datetime import datetime
from library import Book
from file_manager import (
    save_books,
    load_books,
    load_borrow_history,
    save_borrow_history,
    add_borrow_history,
    add_return_history,
)

books = load_books()


welcome_message = """
                                    ==============================
                                    Welcome to the Library Manager
                                    ==============================
"""
menu_options = """
                                        1. View All Books
                                        2. Add Book
                                        3. Search Book(By ID, By Title)
                                        4. Remove Book(By ID, By Title)
                                        5. Borrow Book(By ID or Title)
                                        6. Return Book(By ID or Title)
                                        7. Save
                                        8. Exit
                                        9. View Borrow History
"""



def view_all_books():
    if not books:
        print("No Books Found")
    else:
        for book in books:
            book.display_info()
            print("-" * 30)




def add_book():
    try:
        user_answer1 = input("To add a book, the system requires you to have the following: Title, Author, Release Year, Is Borrowed Status. Do you have the following? ").lower()
        if user_answer1 == "yes":
            user_title = input("Enter Book Title: ").title()
            user_author = input("Enter Author: ").title()
            user_release = input("Enter release year: ")
            if len(user_release) != 4 or not user_release.isdigit():
                print("Invalid: Please enter a 4 digit release year")
                return
            
            user_borrowed = input("Enter Borrow Status(Yes/No): ").title()
            if user_borrowed != "Yes" and user_borrowed != "No":
                print("Invalid input: Please enter Yes or No")
                return
            
            user_id = input("Create a 6 digit ID for the book: ")
            if len(user_id) != 6 or not user_id.isdigit():
                print("Invalid: Please enter a 6 digit number")
                return
            
            for book in books:
                if book.book_id == int(user_id):
                    print("A Book with the same ID already exists. Please Enter A Different ID")
                    return
            
            books.append(Book(user_title, user_author, int(user_release), user_borrowed, int(user_id)))
            print("Book Added Successfully")
        
        elif user_answer1 == "no":
            print("Ok, the system will cancel this request")
        
        else:
            print("Invalid input. Enter yes/no")
    
    except ValueError:
        print("Invalid input: Enter a whole number")



def search_book():
    user_answer2 = input("Enter the book you would like to search for via 6 digit ID: ")
    if len(user_answer2) != 6 or not user_answer2.isdigit():
        print("Invalid Input: Please Enter A 6 Digit ID")
        return
    
    user_answer2 = int(user_answer2)
    for book in books:
        if book.book_id == user_answer2:
            book.display_info()
            return
    
    print("Book Not Found")



def title_search():
    title_user_answer = input("Enter the Title of the Book you would like to search for: ").title()
    for book in books:
        if title_user_answer == book.title:
            book.display_info()
            return
        
    print("Book Not Found")



def remove_book():
    user_answer3 = input("Enter the 6 digit ID of the book you would like to remove: ")
    if len(user_answer3) != 6 or not user_answer3.isdigit():
        print("Invalid input: Please enter a 6 digit ID")
        return
    
    for book in books:
        if book.book_id == int(user_answer3):
            books.remove(book)
            print("Book removed succesfully")
            return
    
    print("Book Not Found")



def title_remove():
    title_user_answer2 = input("Enter The Title of the Book you would like to remove: ").title()
    for book in books:
        if title_user_answer2 == book.title:
            books.remove(book)
            print("Book removed successfully")
            return
    
    print("Book not found")

        

       

def find_book_by_id_or_title(identifier):
    identifier = identifier.strip()
    if not identifier:
        return None

    if len(identifier) == 6 and identifier.isdigit():
        book_id = int(identifier)
        for book in books:
            if book.book_id == book_id:
                return book
        return None

    normalized_title = identifier.title()
    for book in books:
        if book.title.lower() == normalized_title.lower():
            return book

    return None


def borrow_book():
    user_answer4 = input("Enter the 6 digit ID or title of the book you would like to borrow: ")
    book = find_book_by_id_or_title(user_answer4)

    if book is None:
        print("Book Not Found")
        return

    if book.is_borrowed == "Yes":
        print("Book is already being borrowed, please choose another one")
        return

    confirmation = input(f"Are you sure you would like to borrow '{book.title}'? ").lower()

    if confirmation == "yes":
        borrowed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        book.mark_borrowed(borrowed_at)

        history = load_borrow_history()
        history = add_borrow_history(history, book.book_id, borrowed_at)
        save_borrow_history(history)
        return

    if confirmation == "no":
        print("Ok, the system will cancel this request")
        return

    print("Invalid option: Enter yes/no")
    return


def return_book():
    user_answer5 = input("Enter the 6 digit ID or title of the book you would like to return: ")
    book = find_book_by_id_or_title(user_answer5)

    if book is None:
        print("Book Not Found")
        return

    if book.is_borrowed == "No":
        print("Book is already in Library. Are you sure you that is the right book?")
        return

    confirmation2 = input(f"Are you sure you would like to return '{book.title}' now?").lower()
    if confirmation2 == "yes":
        returned_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        book.mark_returned(returned_at)

        history = load_borrow_history()
        history = add_return_history(history, book.book_id, returned_at)
        save_borrow_history(history)
        return

    if confirmation2 == "no":
        print("Ok, the system will cancel the request")
        return

    print("Invalid option, please enter a yes/no")
    return




def view_borrow_history():
    history = load_borrow_history()
    if not history:
        print("No borrow history found")
        return

    user_answer6 = input("Enter the 6 digit ID of the book you want to view history for: ")
    if len(user_answer6) != 6 or not user_answer6.isdigit():
        print("Invalid input: Please enter a 6 digit ID")
        return

    book_id = int(user_answer6)
    for book in books:
        if book.book_id == book_id:
            entries = history.get(str(book_id), [])
            if not entries:
                print("No history found for this book")
                return

            print(f"Borrow History for {book.title} (ID: {book_id})")
            for index, entry in enumerate(entries, start=1):
                borrowed_at = entry.get("borrowed_at") or "Not recorded"
                returned_at = entry.get("returned_at") or "Not returned yet"
                print(f"{index}. Borrowed: {borrowed_at}")
                print(f"   Returned: {returned_at}")
            return

    print("Book Not Found")


def save_program():
    save_books(books)


def exit_program():
    save_books(books)
    print("Goodbye")
    exit()





if __name__ == "__main__":
    print(f"{welcome_message}")
    while  True:
        print(f"{menu_options}")
        try:
            me = int(input("Choose an option: "))
        except ValueError:
            print("Please Enter A number")
            continue
        
        if me == 1:
            view_all_books()
        
        elif me == 2:
            add_book()
        
        elif me == 3:
            try:
                option_to_choose = int(input("Search By: 1. Book ID   2. Title"))
            except ValueError:
                print("Enter 1 or 2")
                continue

            if option_to_choose == 1:
                search_book()
            elif option_to_choose == 2:
                title_search()
            else:
                print("Enter 1 or 2")
        
        elif me == 4:
            try:
                option_to_choose2 = int(input("Remove By: 1. Book ID   2. Title"))
            except ValueError:
                print("Enter 1 or 2")
                continue
            
            if option_to_choose2 == 1:
                remove_book()
            elif option_to_choose2 == 2:
                title_remove()
            else:
                print("Enter 1 or 2")
        
        elif me == 5:
            borrow_book()
        
        elif me == 7:
            save_program()
        
        elif me == 8:
            exit_program()

        elif me == 9:
            view_borrow_history()
        
        elif me == 6:
            return_book()
        
        else:
            print("Invalid Option")
