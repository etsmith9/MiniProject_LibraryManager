#miniproject.py

from book import Book
from user import User
from author import Author

class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.authors = {}
    
    def add_book(self, title, author, genre, pub_date):
        new_book = Book(title, author, genre, pub_date)
        self.books[title] = new_book
        print(f"Book '{title}' added successfully.")
    
    def borrow_book(self, user_id, book_title):
        if book_title in self.books:
            book = self.books[book_title]
            if book.is_available():
                if user_id in self.users:
                    user = self.users[user_id]
                    if user.borrow_book(book):
                        print(f"User '{user.get_name()}' borrowed '{book_title}'.")
                    else:
                        print(f"Failed to borrow book '{book_title}'.")
                else:
                    print(f"User '{user_id}' not found.")
            else:
                print(f"Book '{book_title}' is currently unavailable.")
        else:
            print(f"Book '{book_title}' not found.")

    def return_book(self, user_id, book_title):
        if user_id in self.users:
            user = self.users[user_id]
            book = self.books.get(book_title)
            if book and user.return_book(book):
                print(f"User '{user.get_name()}' returned '{book_title}'.")
            else:
                print(f"Error in returning '{book_title}'.")
        else:
            print(f"User '{user_id}' not found.")

    def search_book(self, title):
        if title in self.books:
            book = self.books[title]
            print(f"Found book: {book.get_title()} by {book.get_author()}")
        else:
            print(f"Book '{title}' not found.")

    def display_books(self):
        if self.books:
            for book in self.books.values():
                availability = "Available" if book.is_available() else "Borrowed"
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, Status: {availability}")
        else:
            print("No books in the library.")

    def add_user(self, name, user_id):
        new_user = User(name, user_id)
        self.users[user_id] = new_user
        print(f"User '{name}' added successfully.")
    
    def view_user(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            borrowed_books = user.get_borrowed_books()
            print(f"User: {user.get_name()}, ID: {user.get_user_id()}, Borrowed Books: {', '.join(borrowed_books)}")
        else:
            print(f"User '{user_id}' not found.")

    def display_users(self):
        if self.users:
            for user in self.users.values():
                print(f"User: {user.get_name()}, ID: {user.get_user_id()}")
        else:
            print("No users in the system.")

    def add_author(self, name, biography):
        new_author = Author(name, biography)
        self.authors[name] = new_author
        print(f"Author '{name}' added successfully.")
    
    def view_author(self, name):
        if name in self.authors:
            author = self.authors[name]
            print(f"Author: {author.get_name()}, Biography: {author.get_biography()}")
        else:
            print(f"Author '{name}' not found.")

    def display_authors(self):
        if self.authors:
            for author in self.authors.values():
                print(f"Author: {author.get_name()}")
        else:
            print("No authors in the system.")

    def show_main_menu(self):
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
    
    def show_book_menu(self):
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
    
    def show_user_menu(self):
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
    
    def show_author_menu(self):
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")

def main():
    system = LibraryManagementSystem()

    while True:
        system.show_main_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":  
            system.show_book_menu()
            book_choice = input("Enter your choice: ").strip()
            
            if book_choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                genre = input("Enter book genre: ")
                pub_date = input("Enter publication date: ")
                system.add_book(title, author, genre, pub_date)
            
            elif book_choice == "2":
                user_id = input("Enter user ID: ")
                book_title = input("Enter book title to borrow: ")
                system.borrow_book(user_id, book_title)
            
            elif book_choice == "3":
                user_id = input("Enter user ID: ")
                book_title = input("Enter book title to return: ")
                system.return_book(user_id, book_title)
            
            elif book_choice == "4":
                title = input("Enter book title to search: ")
                system.search_book(title)
            
            elif book_choice == "5":
                system.display_books()
        
        elif choice == "2": 
            system.show_user_menu()
            user_choice = input("Enter your choice: ").strip()
            
            if user_choice == "1":
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                system.add_user(name, user_id)
            
            elif user_choice == "2":
                user_id = input("Enter user ID: ")
                system.view_user(user_id)
            
            elif user_choice == "3":
                system.display_users()
        
        elif choice == "3":  
            system.show_author_menu()
            author_choice = input("Enter your choice: ").strip()
            
            if author_choice == "1":
                name = input("Enter author name: ")
                biography = input("Enter author biography: ")
                system.add_author(name, biography)
            
            elif author_choice == "2":
                name = input("Enter author name: ")
                system.view_author(name)
            
            elif author_choice == "3":
                system.display_authors()
        
        elif choice == "4": 
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
