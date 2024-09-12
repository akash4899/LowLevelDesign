from threading import Lock
from book import Book
from book_catalogue import BookCatalogue
from member import Member
from uuid import uuid4


class LibraryManagementSystem:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.book_catalogue = BookCatalogue()
                cls._instance.members = []

        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def add_member(self, member):
        # member_id = self.generate_member_id()
        self.members.append(member)

    def add_book(self, book):
        # book = Book(self.generate_member_id(), title, isbn_number, publication_year)

        self.book_catalogue.add_book(book)

    def remove_book(self, book):
        self.book_catalogue.remove_book(book)

    def search_book(self, title):
        book = self.book_catalogue.search_book(title)
        if book:
            print("Book found")
            return
        print("Book Not found")

    def borrow_book(self, member, book):
        book_required = self.book_catalogue.search_book(book)
        for self_member in self.members:
            if member == self_member.member_id:
                self_member.borrow_book(book_required)
                book_required.borrow_book()
        print("Member not found")

    def return_book(self, member, book):
        for self_member in self.members:
            if member == self_member.member_id:
                self_member.borrow_book(book)
        print("Member not found")

    def generate_member_id(self):
        return f"MEM{uuid4().hex[:8].upper()}"
