class Book:
    
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out
       
        
class Library():
    books = []
    def __init__(self):
        self._books = []
    def add_book(self, book):
        Library.books.append(book)
        
        
    def check_out_book(self, title):
        for book in Library.books:
            if book.title == title:
                book.is_checked_out = True
                
        
    def return_book(self):
        ...         
    def return_book(self, title):
        for book in Library.books:
            if book.title == title:
                book.is_checked_out = False
        
    def list_available_books(self):
        for book in Library.books:
            if book.is_checked_out == False:
                print(f"{book.title} by {book.author} ")
        
# library = Library()
# library.add_book(Book("Brave New World", "Aldous Huxley"))
# library.add_book(Book("1984", "George Orwell"))

# print("Available books after setup:")
# library.list_available_books()
# library.check_out_book("1984")
# print("\nAvailable books after checking out '1984':")
# library.list_available_books()
# library.return_book("1984")
# print("\nAvailable books after returning '1984':")
# library.list_available_books()
