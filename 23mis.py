class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def show_available_books(self):
        print("\n--- Available Books ---")
        available = [b for b in self.books if not b.is_issued]
        if not available:
            print("No books currently available.")
        for i, book in enumerate(available, 1):
            print(f"{i}. {book.title} by {book.author}")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_issued:
                book.is_issued = True
                print(f"You have borrowed '{book.title}'.")
                return
        print("Sorry, book not found or already issued.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_issued:
                book.is_issued = False
                print(f"Thank you for returning '{book.title}'.")
                return
        print("Invalid return attempt.")

# --- Main Program Loop ---
def main():
    my_library = Library()
    # Adding some starter books
    my_library.add_book("Python Crash Course", "Eric Matthes")
    my_library.add_book("Clean Code", "Robert Martin")

    while True:
        print("\nWelcome to the Library Management System")
        print("1. List Books\n2. Add Book\n3. Borrow Book\n4. Return Book\n5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            my_library.show_available_books()
        elif choice == '2':
            t = input("Enter Title: ")
            a = input("Enter Author: ")
            my_library.add_book(t, a)
        elif choice == '3':
            t = input("Enter the title of the book to borrow: ")
            my_library.issue_book(t)
        elif choice == '4':
            t = input("Enter the title of the book to return: ")
            my_library.return_book(t)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()