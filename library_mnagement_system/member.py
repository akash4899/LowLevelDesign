
class Member:
    def __init__(self, member_id, name, contact):
        self.member_id = member_id
        self.name = name
        self.contact = contact
        self.borrowed_books = []
        self.borrowing_history = None

    def borrow_book(self, book):
        if len(self.borrowed_books)>5:
            print("Borrowing limit exceeded.")
        else:
            self.borrowed_books.append(book)
            # print("Book alloted.")

    def return_book(self, book_name):
        for book in self.borrowed_books:
            if book.get_title() == book_name:
                self.borrowed_books.remove(book)
                book.return_book()
                return
        print("Book not found.")
        return

