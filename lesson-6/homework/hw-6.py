##Zero Chek Decorator

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

print(div(6, 2)) 
print(div(6, 0))  


##Employee Records manager

import os

FILENAME = "employees.txt"

def add_employee():
    with open(FILENAME, "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully.\n")

def view_employees():
    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()
            if records:
                print("\nAll Employee Records:")
                for line in records:
                    print(line.strip())
            else:
                print("No records found.\n")
    except FileNotFoundError:
        print("No records found.\n")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Employee Found:", line.strip())
                    found = True
                    break
        if not found:
            print("Employee not found.\n")
    except FileNotFoundError:
        print("No records found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated = False
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        with open(FILENAME, "w") as file:
            for line in lines:
                if line.startswith(emp_id + ","):
                    print("Current record:", line.strip())
                    name = input("Enter new name: ")
                    position = input("Enter new position: ")
                    salary = input("Enter new salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Employee updated successfully.\n")
        else:
            print("Employee ID not found.\n")
    except FileNotFoundError:
        print("No records found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    deleted = False
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        with open(FILENAME, "w") as file:
            for line in lines:
                if not line.startswith(emp_id + ","):
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("Employee deleted successfully.\n")
        else:
            print("Employee ID not found.\n")
    except FileNotFoundError:
        print("No records found.\n")

def menu():
    while True:
        print("\nEmployee Record Management System")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()



##Word Frequency Counter

import os
import string
from collections import Counter

def create_file():
    print("sample.txt not found. Please enter a paragraph to create the file:")
    text = input("Enter paragraph:\n")
    with open("sample.txt", "w") as file:
        file.write(text)
    print("sample.txt created.\n")

def clean_text(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator).lower()

def count_words():
    if not os.path.exists("sample.txt"):
        create_file()

    with open("sample.txt", "r") as file:
        content = file.read()

    cleaned = clean_text(content)
    words = cleaned.split()
    total_words = len(words)
    word_counts = Counter(words)
    top_5 = word_counts.most_common(5)

    print(f"\nTotal words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5:
        print(f"{word} - {count} {'time' if count == 1 else 'times'}")

    with open("word_count_report.txt", "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in top_5:
            report.write(f"{word} - {count}\n")

    print("\nReport saved to 'word_count_report.txt'.")

if __name__ == "__main__":
    count_words()


##Bonus Tasks

import os, string
from collections import Counter

def clean_line(line):
    return line.translate(str.maketrans('', '', string.punctuation)).lower().split()

def get_top_words():
    if not os.path.exists("sample.txt"):
        with open("sample.txt", "w") as f:
            f.write(input("sample.txt not found. Enter a paragraph:\n"))

    counter = Counter()
    total = 0

    with open("sample.txt", "r") as f:
        for line in f:
            words = clean_line(line)
            counter.update(words)
            total += len(words)

    while True:
        try:
            top_n = int(input("How many top common words to display? "))
            if top_n > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    top_words = counter.most_common(top_n)

    print(f"\nTotal words: {total}\nTop {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} {'time' if count == 1 else 'times'}")

    with open("word_count_report.txt", "w") as out:
        out.write(f"Word Count Report\nTotal Words: {total}\nTop {top_n} Words:\n")
        for word, count in top_words:
            out.write(f"{word} - {count}\n")

if __name__ == "__main__":
    get_top_words()


   


