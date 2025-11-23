class Book:
    def __init__(self, title, author, isbn, status='available'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def is_available(self):
        """Return True if the book is available for issuing."""
        return self.status == 'available'

    def issue_book(self):
        if self.status == 'available':
            self.status = 'issued'
            print(f'Book "{self.title}" has been issued.')
        else:
            print(f'Book "{self.title}" is not available for issuing.')

    def reserve_book(self):
        if self.status == 'available':
            self.status = 'reserved'
            print(f'Book "{self.title}" has been reserved.')
        else:
            print(f'Book "{self.title}" is not available for reserving.')

    def return_book(self):
        if self.status in ['issued', 'reserved']:
            self.status = 'available'
            print(f'Book "{self.title}" has been returned and is now available.')
        else:
            print(f'Book "{self.title}" was not issued or reserved.')

    def check_status(self):
        print(f'Book "{self.title}" is currently {self.status}.')
        return self.status