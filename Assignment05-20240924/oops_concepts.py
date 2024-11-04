# -*- coding: utf-8 -*-
"""Assignment4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kAHmyI32fgp7AdM-q41TjTCgY5fcqCJ1
"""

# Create a database of books log using oops concept

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class BookLog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f'Book "{title}" added to the log.')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Book "{title}" removed from the log.')
                return
        print(f'Book "{title}" not found.')

    def display_books(self):
        if not self.books:
            print("No books in the log.")
        else:
            print("Books in the log:")
            for book in self.books:
                print(f"- {book}")

if __name__ == "__main__":
    my_book_log = BookLog()

    my_book_log.add_book("Mockingbird", "Lee", 1960)

    my_book_log.display_books()

    my_book_log.remove_book("The Great")

    my_book_log.display_books()