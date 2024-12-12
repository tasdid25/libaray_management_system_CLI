import json
from datetime import datetime, timedelta

from file_handler import save_all_books, save_lend_books


def lend_book(all_books, lend_books):
    book_title = input("Enter the title of the book to lend: ")
    for book in all_books:
        if book["title"] == book_title:
            if book["quantity"] > 0:
                borrower_name = input("Enter borrower's name: ")
                phone_number = input("Enter borrower's phone number: ")
                due_date = datetime.now() + timedelta(days=14)  # 2 weeks from now

                lend_info = {
                    "title": book_title,
                    "borrower_name": borrower_name,
                    "phone_number": phone_number,
                    "due_date": due_date.strftime("%d-%m-%Y")
                }

                lend_books.append(lend_info)
                save_lend_books(lend_books)

                book["quantity"] -= 1
                save_all_books(all_books)
                print(
                    f"Book '{book_title}' lent successfully to {borrower_name}. Due date: {due_date.strftime('%d-%m-%Y')}.")
                return
            else:
                print("There are not enough books available to lend.")
                return
    print("Book not found.")


def return_book(all_books, lend_books):
    book_title = input("Enter the title of the book to return: ")
    borrower_name = input("Enter borrower's name: ")

    for lend_info in lend_books:
        if lend_info["title"] == book_title and lend_info["borrower_name"] == borrower_name:
            lend_books.remove(lend_info)
            save_lend_books(lend_books)

            for book in all_books:
                if book["title"] == book_title:
                    book["quantity"] += 1
                    save_all_books(all_books)
                    print(f"Book '{book_title}' returned successfully by {borrower_name}.")
                    return

    print("No matching lending record found.")
