
class Book:
    total_books = 0     # Class variable to check total books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()     # Call class method when the book is added

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
# Creating objects for Books
book1 = Book("Raja Gidh - Bano Qudsia")
book2 = Book("Peer-e-Kamil - Umera Ahmed")
book3 = Book("Aag Ka Darya - Qurat-ul-Ain Haider")
book4 = Book("Hasil Ghaat - Intizar Hussain")

# Displaying total number of books
print(f"Total books added: {Book.get_total_books()}")