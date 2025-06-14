# test_library_management.py

import unittest
from library_management import Book, Library

class TestLibraryManagement(unittest.TestCase):

    def test_book_checkout_and_return(self):
        book = Book("Test Title", "Test Author")
        self.assertTrue(book.is_available())
        self.assertTrue(book.check_out())
        self.assertFalse(book.is_available())
        self.assertFalse(book.check_out())  # Already checked out
        self.assertTrue(book.return_book())
        self.assertTrue(book.is_available())
        self.assertFalse(book.return_book())  # Already returned

    def test_library_add_and_list_books(self):
        library = Library()
        book1 = Book("Book 1", "Author 1")
        book2 = Book("Book 2", "Author 2")

        library.add_book(book1)
        library.add_book(book2)

        # Both should be available
        available_titles = [book.title for book in library._books if book.is_available()]
        self.assertIn("Book 1", available_titles)
        self.assertIn("Book 2", available_titles)

    def test_check_out_and_return_book(self):
        library = Library()
        book = Book("Sample Book", "Author")
        library.add_book(book)

        self.assertTrue(library.check_out_book("Sample Book"))
        self.assertFalse(book.is_available())

        self.assertFalse(library.check_out_book("Sample Book"))  # Already checked out

        self.assertTrue(library.return_book("Sample Book"))
        self.assertTrue(book.is_available())

        self.assertFalse(library.return_book("Sample Book"))  # Already returned

    def test_nonexistent_book(self):
        library = Library()
        self.assertFalse(library.check_out_book("Unknown Book"))
        self.assertFalse(library.return_book("Unknown Book"))

if __name__ == '__main__':
    unittest.main()
