import json


def save_all_books(all_books):
    with open("all_books.json", "w") as fp:
        json.dump(all_books, fp, indent=4)


def view_all_books(all_books):
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)

    if all_books != []:
        for book in all_books:
            print(
                f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}")
    else:
        print("No Book found.")


def load_all_books():
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)
    return all_books


def load_lend_books():
    try:
        with open("lend_books.json", "r") as fp:
            return json.load(fp)
    except FileNotFoundError:
        return []


def save_lend_books(lend_books):
    with open("lend_books.json", "w") as fp:
        json.dump(lend_books, fp, indent=4)
