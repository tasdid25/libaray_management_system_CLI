import random
from datetime import datetime
from file_handler import save_all_books


def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    # isbn = int(input("Enter ISBN Number: "))

    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            year = int(input("Enter Publishing Year Number: "))
            price = int(input("Enter Book Price: "))
            break
        except Exception as e:
            print("Please enter a valid value.")

    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt,
        "bookLastUpdatedAt": ""
    }

    all_books.append(book)
    save_all_books(all_books)

    print("Books Added Successully")

    return all_books


def delete_books(all_books):
    search_book = input("Enter Book Title to Delete: ")
    for book in all_books:
        if book["title"] == search_book:
            all_books.remove(book)
            save_all_books.save_all_books(all_books)
            print("Book Deleted Successfully")
            return all_books

    print("Book Not Found")


def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    for book in all_books:
        if book["title"] == search_book:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = int(input("Enter Publishing Year Number: "))
            price = int(input("Enter Book Price: "))
            quantity = int(input("Enter Quantity Number: "))

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["bookLastUpdatedAt"] = book_last_updated_at

            save_all_books(all_books)
            print("Book Updated Successfully")
            return all_books

    print("Book Not Found")
