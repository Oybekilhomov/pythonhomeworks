

import math

class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("Vector must have at least one component.")
        self.components = tuple(float(c) for c in components)
    
    def __str__(self):
        return f"Vector{self.components}"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.components)
    
    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension.")
    
    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported operand type for *")
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ZeroDivisionError("Cannot normalize a zero vector.")
        return Vector(*[a / mag for a in self.components])

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)
print(v1 = v2)
print(v2 - v1)
print(v1 * v2)
print(3 * v1)
print(v1.magnitude())
print(v1.normalize())



import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        employee = Employee(employee_id, name, position, salary)
        with open(self.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")

        print("Employee added successfully!")

    def view_employees(self):
        if not os.path.exists(self.FILE_NAME):
            print("No employee records found.")
            return

        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for line in lines:
                print(line.strip())

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        found = False

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Employee Found:\n" + line.strip())
                    found = True
                    break

        if not found:
            print("Employee not found.")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        updated = False

        if not os.path.exists(self.FILE_NAME):
            print("No employee records found.")
            return

        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(self.FILE_NAME, "w") as file:
            for line in lines:
                if line.startswith(emp_id + ","):
                    print("Current Record: " + line.strip())
                    name = input("Enter new name: ")
                    position = input("Enter new position: ")
                    salary = input("Enter new salary: ")
                    updated_line = f"{emp_id}, {name}, {position}, {salary}\n"
                    file.write(updated_line)
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        deleted = False

        if not os.path.exists(self.FILE_NAME):
            print("No employee records found.")
            return

        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(self.FILE_NAME, "w") as file:
            for line in lines:
                if line.startswith(emp_id + ","):
                    deleted = True
                else:
                    file.write(line)

        if deleted:
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")

    def run(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run()



import json
import csv
from abc import ABC, abstractmethod
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "Task ID": self.task_id,
            "Title": self.title,
            "Description": self.description,
            "Due Date": self.due_date,
            "Status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["Task ID"],
            data["Title"],
            data["Description"],
            data.get("Due Date"),
            data.get("Status", "Pending")
        )

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass

class JSONStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load(self, filename):
        with open(filename, 'r') as f:
            return [Task.from_dict(data) for data in json.load(f)]

class CSVStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Task ID", "Title", "Description", "Due Date", "Status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            return [Task.from_dict(row) for row in reader]

class ToDoManager:
    def __init__(self, storage_strategy: StorageStrategy):
        self.tasks = []
        self.storage_strategy = storage_strategy

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = kwargs.get("title", task.title)
                task.description = kwargs.get("description", task.description)
                task.due_date = kwargs.get("due_date", task.due_date)
                task.status = kwargs.get("status", task.status)
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def filter_tasks(self, status):
        return [task for task in self.tasks if task.status == status]

    def save_tasks(self, filename):
        self.storage_strategy.save(self.tasks, filename)

    def load_tasks(self, filename):
        self.tasks = self.storage_strategy.load(filename)

def main():
    storage = JSONStorage() 
    manager = ToDoManager(storage)

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            task = Task(task_id, title, description, due_date, status)
            manager.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            tasks = manager.view_tasks()
            print("Tasks:")
            for task in tasks:
                print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

        elif choice == '3':
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title: ")
            description = input("Enter new Description: ")
            due_date = input("Enter new Due Date (YYYY-MM-DD): ")
            status = input("Enter new Status: ")
            if manager.update_task(task_id, title=title, description=description, due_date=due_date, status=status):
                print("Task updated successfully!")
            else:
                print("Task not found.")

        elif choice == '4':
            task_id = input("Enter Task ID to delete: ")
            if manager.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task not found.")

        elif choice == '5':
            status = input("Enter status to filter by: ")
            tasks = manager.filter_tasks(status)
            for task in tasks:
                print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

        elif choice == '6':
            filename = input("Enter filename to save tasks: ")
            manager.save_tasks(filename)
            print("Tasks saved successfully!")

        elif choice == '7':
            filename = input("Enter filename to load tasks: ")
            manager.load_tasks(filename)
            print("Tasks loaded successfully!")

        elif choice == '8':
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



