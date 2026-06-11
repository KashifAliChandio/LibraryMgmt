# Library Management System

library = {
    "101": {"title": "Python Basics", "issued": False},
    "102": {"title": "Data Structures", "issued": True},
    "103": {"title": "Machine Learning", "issued": False},
    "104": {"title": "Artificial Intelligence", "issued": True},
    "105": {"title": "Database Systems", "issued": False},
    "106": {"title": "Computer Networks", "issued": False},
    "107": {"title": "Operating Systems", "issued": True},
    "108": {"title": "Software Engineering", "issued": False},
    "109": {"title": "Cyber Security", "issued": False},
    "110": {"title": "Cloud Computing", "issued": True},
    "111": {"title": "Deep Learning", "issued": False},
    "112": {"title": "Natural Language Processing", "issued": False},
    "113": {"title": "Web Development", "issued": True},
    "114": {"title": "Java Programming", "issued": False},
    "115": {"title": "C++ Programming", "issued": False},
    "116": {"title": "Algorithms", "issued": True},
    "117": {"title": "Discrete Mathematics", "issued": False},
    "118": {"title": "Computer Graphics", "issued": False},
    "119": {"title": "Data Science Handbook", "issued": True},
    "120": {"title": "Introduction to AI", "issued": False}
}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")

    if book_id in library:
        print("Book already exists!")
    else:
        library[book_id] = {"title": title, "issued": False}
        print("Book added successfully!")


def remove_book():
    book_id = input("Enter Book ID to remove: ")

    if book_id in library:
        del library[book_id]
        print("Book removed successfully!")
    else:
        print("Book not found!")


def search_book():
    title = input("Enter Book Title: ").lower()

    for book_id, details in library.items():
        if title in details["title"].lower():
            print(
                f"Book ID: {book_id}, Title: {details['title']}, Issued: {details['issued']}"
            )
            return

    print("Book not found!")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    if book_id in library:
        if library[book_id]["issued"]:
            print("Book is already issued!")
        else:
            library[book_id]["issued"] = True
            print("Book issued successfully!")
    else:
        print("Book not found!")


def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id in library:
        if library[book_id]["issued"]:
            library[book_id]["issued"] = False
            print("Book returned successfully!")
        else:
            print("Book was not issued!")
    else:
        print("Book not found!")


def display_books():
    print("\n===== LIBRARY BOOKS =====")

    for book_id, details in library.items():
        status = "Issued" if details["issued"] else "Available"

        print(
            f"Book ID: {book_id:<5} "
            f"Title: {details['title']:<35} "
            f"Status: {status}"
        )


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Display Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        display_books()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!, Please Enter number only")