class BookNotFoundException(Exception):
    """Exception raised when a book is not found in the library."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Exception raised when attempting to borrow a book that is already borrowed."""
    pass

class MemberLimitExceededException(Exception):
    """Exception raised when a member tries to borrow more than the allowed limit of books."""
    pass

class Book:
    """Represents a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    """Represents a library member who can borrow books."""
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """Allows the member to borrow a book if they have not exceeded the limit."""
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title}")

    def return_book(self, book):
        """Allows the member to return a borrowed book."""
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have {book.title} to return.")

    def __str__(self):
        return f"{self.name} (Borrowed Books: {', '.join([book.title for book in self.borrowed_books]) or 'None'})"

class Library:
    """Represents the library system, managing books and members."""
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self.books.append(book)
        print(f"Added book: {book.title}")

    def add_member(self, member):
        """Registers a new member to the library."""
        self.members.append(member)
        print(f"Added member: {member.name}")

    def borrow_book(self, member_name, book_title):
        """Allows a member to borrow a book if it is available."""
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        """Allows a member to return a borrowed book."""
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if member and book:
            member.return_book(book)
        else:
            print(f"Could not process return. Check member and book details.")

# Testing the system
library = Library()

# Adding books
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_book(Book("Moby-Dick", "Herman Melville"))

# Adding members
library.add_member(Member("Alice"))
library.add_member(Member("Bob"))

# Borrowing books
try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "Moby-Dick")
    library.borrow_book("Alice", "Another Book")  # Should raise BookNotFoundException
except Exception as e:
    print(e)

# Exceeding book limit
try:
    library.borrow_book("Alice", "1984")  # Should raise BookAlreadyBorrowedException
except Exception as e:
    print(e)

# Returning books
library.return_book("Alice", "1984")
library.return_book("Bob", "1984")  # Bob never borrowed it

# Checking status
for member in library.members:
    print(member)

for book in library.books:
    print(book)
