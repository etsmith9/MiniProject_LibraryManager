class User:
    def __init__(self, name, user_id):
        self.__name = name
        self.__user_id = user_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_user_id(self):
        return self.__user_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book.get_title())
            return True
        return False

    def return_book(self, book):
        if book.get_title() in self.__borrowed_books:
            self.__borrowed_books.remove(book.get_title())
            book.return_book()
            return True
        return False
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography
