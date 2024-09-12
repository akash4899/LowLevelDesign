from book import Book

class BookCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.upper() == title.upper():
                print(book.title.upper(), title.upper())
                return book
        return None