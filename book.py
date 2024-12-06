class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__available = True 

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_pub_date(self):
        return self.__pub_date

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True
