
# Library Management System
# A simple menu-driven program using basic Python concepts
 
books = {}      # book_id -> {"title", "author", "total", "available"}
issued = []     # list of {"member", "book_id"} for books currently issued
LOAN_DAYS = 14
FINE_PER_DAY = 2
 
def add_book():
    book_id = input("Enter book ID : ").strip().upper()
    if book_id in books:
        print("Book ID already exists.")
        return
    title = input("Enter title   : ").strip().title()
    author = input("Enter author  : ").strip().title()
    try:
        copies = int(input("Number of copies: "))
    except ValueError:
        print("Invalid input. Copies must be a number.")
        return
    if copies <= 0:
        print("Copies must be greater than zero.")
        return
    books[book_id] = {"title": title, "author": author,
                      "total": copies, "available": copies}
    print(f"Book '{title}' added successfully.")
 
def view_books():
    if not books:
        print("No books in the library.")
        return
    print(f"{'ID':<7}{'Title':<28}{'Author':<18}{'Avail'}")
    print("-" * 59)
    for book_id, b in books.items():
        print(f"{book_id:<7}{b['title']:<28}{b['author']:<18}"
              f"{b['available']}/{b['total']}")
 
def search_book():
    word = input("Enter title or author to search: ").strip().lower()
    found = False
    for book_id, b in books.items():
        if word in b["title"].lower() or word in b["author"].lower():
            print(f"{book_id} | {b['title']} | {b['author']} | "
                  f"Available: {b['available']}")
            found = True
    if not found:
        print("No matching book found.")
 
def issue_book():
    book_id = input("Enter book ID to issue: ").strip().upper()
    if book_id not in books:
        print("Book not found.")
        return
    if books[book_id]["available"] == 0:
        print("Sorry, no copies are available.")
        return
    member = input("Enter member name: ").strip().title()
    books[book_id]["available"] -= 1
    issued.append({"member": member, "book_id": book_id})
    print(f"'{books[book_id]['title']}' issued to {member}.")
 


def return_book():
    book_id = input("Enter book ID to return: ").strip().upper()
    member = input("Enter member name: ").strip().title()
    for record in issued:
        if record["book_id"] == book_id and record["member"] == member:
            try:
                days = int(input("Days kept: "))
            except ValueError:
                print("Invalid input. Days must be a number.")
                return
            issued.remove(record)
            books[book_id]["available"] += 1
            fine = max(0, days - LOAN_DAYS) * FINE_PER_DAY
            print("Book returned successfully.")
            print(f"Fine to pay: Rs. {fine}")
            return
    print("No such issue record found.")
 
def library_report():
    total_titles = len(books)
    total_copies = sum(b["total"] for b in books.values())
    available = sum(b["available"] for b in books.values())
    print(f"Total titles     : {total_titles}")
    print(f"Total copies     : {total_copies}")
    print(f"Copies available : {available}")
    print(f"Copies issued    : {len(issued)}")
 
def save_to_file():
    with open("library.txt", "w") as file:
        for book_id, b in books.items():
            file.write(f"{book_id},{b['title']},{b['author']},"
                       f"{b['total']},{b['available']}\n")
    print("Records saved to library.txt")
 
actions = {"1": add_book, "2": view_books, "3": search_book,
           "4": issue_book, "5": return_book,
           "6": library_report, "7": save_to_file}
 
def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add book")
        print("2. View all books")
        print("3. Search book")
        print("4. Issue book")
        print("5. Return book")
        print("6. Library report")
        print("7. Save to file")
        print("8. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "8":
            print("Thank you. Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please try again.")
 
main()
