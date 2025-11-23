import os
from library_manager.book import Book


class Library:
    def __init__(self):
        self.catalog = {}
        # default to the packaged data file inside the package's `data/` directory
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.catalog_filename = os.path.join(self.data_dir, 'library_catalog.txt')

    def add_book(self, book):
        self.catalog[book.title] = book
        # logger.info('Added book to catalog: %s (ISBN: %s)', book.title, book.isbn)
        print(f'Book "{book.title}" added to the library catalog.')

    def issue_book(self, title):
        if title in self.catalog:
            self.catalog[title].issue_book()
        else:
            # logger.warning('Issue attempt for missing book title: %s', title)
            print('Book not found in the catalog.')

    def reserve_book(self, title):
        if title in self.catalog:
            self.catalog[title].reserve_book()
        else:
            # logger.warning('Reserve attempt for missing book title: %s', title)
            print('Book not found in the catalog.')

    def return_book(self, title):
        if title in self.catalog:
            self.catalog[title].return_book()
        else:
            # logger.warning('Return attempt for missing book title: %s', title)
            print('Book not found in the catalog.')

    def check_book_status(self, title):
        if title in self.catalog:
            self.catalog[title].check_status()
        else:
            # logger.warning('Status check for missing book title: %s', title)
            print('Book not found in the catalog.')

    def display_catalog(self):
        if not self.catalog:
            print('The catalog is empty.')
        else:
            print('\n--- Library Catalog ---')
            for title, book in self.catalog.items():
                print(f'Title: {title}, Author: {book.author}, ISBN: {book.isbn}, Status: {book.status}')
            print('--- End of Catalog ---\n')

    def update_book(self, current_title, new_title=None, author=None, isbn=None):
        if current_title in self.catalog:
            book = self.catalog[current_title]
            if new_title and new_title != current_title:
                book.title = new_title
                self.catalog[new_title] = book
                del self.catalog[current_title]
                current_title = new_title
            if author:
                book.author = author
            if isbn:            
                book.isbn = isbn
            # logger.info('Updated book: %s (ISBN: %s)', book.title, book.isbn)
            print(f'Book "{book.title}" has been updated successfully.')
        else:
            print('Book not found in the catalog.')
            # logger.warning('Attempted update for missing book title: %s', current_title)
        self.catalog_filename = 'library_catalog.txt'

    