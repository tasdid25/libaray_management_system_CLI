

from file_handler import load_all_books, view_all_books, load_lend_books
from book_manager import update_books, delete_books, add_books
from lend_return_manager import lend_book, return_book

all_books = []
lend_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend Book")
    print("6. Return Book")

    all_books = load_all_books()
    lend_books = load_lend_books()

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books = add_books(all_books)
    elif menu == "2":
        view_all_books(all_books)
    elif menu == "3":
        update_books(all_books)
    elif menu == "4":
        delete_books(all_books)
    elif menu == "5":
        lend_book(all_books, lend_books)
    elif menu == "6":
        return_book(all_books, lend_books)
    else:
        print("Choose a valid number")
