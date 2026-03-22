class Book:
    def __init__(self, name):
        self.name = name
        self.issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        name = input("Enter book name: ")
        self.books.append(Book(name))
        print("Book added!")

    def show_books(self):
        print("\nBooks in Library:")
        for b in self.books:
            status = "Issued" if b.issued else "Available"
            print(b.name, "-", status)

    def issue_book(self):
        name = input("Enter book name to issue: ")
        for b in self.books:
            if b.name == name and not b.issued:
                b.issued = True
                print("Book issued!")
                return
        print("Book not available!")

    def return_book(self):
        name = input("Enter book name to return: ")
        for b in self.books:
            if b.name == name and b.issued:
                b.issued = False
                print("Book returned!")
                return
        print("Invalid book name!")

lib = Library()
while True:
    print("\n1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.show_books()
    elif choice == 3:
        lib.issue_book()
    elif choice == 4:
        lib.return_book()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")