
##Task1


class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < 3

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author):
        self.books[title] = Book(title, author)
        print(f"Book '{title}' by {author} added.")

    def add_member(self, name):
        self.members[name] = Member(name)
        print(f"Member '{name}' added.")

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"Book '{book_title}' not found.")

        book = self.books[book_title]
        member = self.members.get(member_name)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed.")

        if not member.can_borrow():
            raise MemberLimitExceededException(f"{member_name} has exceeded the borrow limit.")

        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"{member_name} borrowed '{book_title}'.")

    def return_book(self, member_name, book_title):
        member = self.members.get(member_name)
        book = self.books.get(book_title)

        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{member_name} returned '{book_title}'.")
        else:
            print(f"{member_name} does not have '{book_title}' borrowed.")

def test_library_system():
    library = Library()

    library.add_book("1984", "George Orwell")
    library.add_book("The Hobbit", "J.R.R. Tolkien")
    library.add_book("Python 101", "Michael Driscoll")

    library.add_member("Alice")
    library.add_member("Bob")

    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "The Hobbit")
        library.borrow_book("Alice", "Python 101")
        library.borrow_book("Alice", "Unknown Book")  
    except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
        print(e)

    try:
        library.add_book("Extra Book", "Author X")
        library.borrow_book("Alice", "Extra Book")
    except MemberLimitExceededException as e:
        print(e)

    try:
        library.borrow_book("Bob", "1984")
    except BookAlreadyBorrowedException as e:
        print(e)

    library.return_book("Alice", "1984")

    library.borrow_book("Bob", "1984")

if __name__ == "__main__":
    test_library_system()


##Task2


class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < 3

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author):
        self.books[title] = Book(title, author)
        print(f"Book '{title}' by {author} added.")

    def add_member(self, name):
        self.members[name] = Member(name)
        print(f"Member '{name}' added.")

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"Book '{book_title}' not found.")

        book = self.books[book_title]
        member = self.members.get(member_name)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed.")

        if not member.can_borrow():
            raise MemberLimitExceededException(f"{member_name} has exceeded the borrow limit.")

        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"{member_name} borrowed '{book_title}'.")

    def return_book(self, member_name, book_title):
        member = self.members.get(member_name)
        book = self.books.get(book_title)

        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{member_name} returned '{book_title}'.")
        else:
            print(f"{member_name} does not have '{book_title}' borrowed.")

def test_library_system():
    library = Library()

    library.add_book("1984", "George Orwell")
    library.add_book("The Hobbit", "J.R.R. Tolkien")
    library.add_book("Python 101", "Michael Driscoll")

    library.add_member("Alice")
    library.add_member("Bob")

    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "The Hobbit")
        library.borrow_book("Alice", "Python 101")
        library.borrow_book("Alice", "Unknown Book")  
    except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
        print(e)

    try:
        library.add_book("Extra Book", "Author X")
        library.borrow_book("Alice", "Extra Book")
    except MemberLimitExceededException as e:
        print(e)

    try:
        library.borrow_book("Bob", "1984")
    except BookAlreadyBorrowedException as e:
        print(e)

    library.return_book("Alice", "1984")

    library.borrow_book("Bob", "1984")

if __name__ == "__main__":
    test_library_system()


##Task3

import json
import csv

TASKS_FILE = 'tasks.json'
CSV_FILE = 'tasks.csv'

def load_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def display_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    average_priority = round(sum(t['priority'] for t in tasks) / total, 2) if total > 0 else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {average_priority}")

def convert_to_csv(tasks):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ID', 'Task', 'Completed', 'Priority'])
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })
    print(f"\nTasks successfully written to {CSV_FILE}.")

def main():
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_to_csv(tasks)

    tasks[0]['completed'] = True
    save_tasks(tasks)
    print("\nUpdated first task as completed and saved.")

if __name__ == '__main__':
    main()


