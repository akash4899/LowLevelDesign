from enum import Enum

class Status(Enum):
    AVAILABLE = 'Available'
    BORROWED = 'Borrowed'

class Book:
    def __init__(self, id, title, isbn_number, publication_year):
        self.id = id
        self.title = title
        self.isbn_number = isbn_number
        self.publication_year = publication_year
        self.availability_status = Status.BORROWED

    def borrow_book(self):
        if self.availability_status == Status.AVAILABLE:
            self.availability_status = Status.BORROWED
            print("Book Alloted.")
        else:
            print("Book is already borrowed by someone.")

    def return_book(self):
        if self.availability_status == Status.BORROWED:
            self.availability_status = Status.AVAILABLE
            print("Book is available now.")
        else:
            print("Book is already available.")

    def get_title(self):
        return self.title

