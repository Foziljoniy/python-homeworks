import json
import csv
from abc import ABC, abstractmethod

class Task:
    """Represents a single task in the To-Do application."""
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class StorageStrategy(ABC):
    """Abstract base class to define storage strategy."""
    
    @abstractmethod
    def save(self, tasks, filename):
        pass
    
    @abstractmethod
    def load(self, filename):
        pass

class JSONStorage(StorageStrategy):
    """Handles saving and loading tasks in JSON format."""
    
    def save(self, tasks, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in tasks], file, indent=4)
    
    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                return [Task(**data) for data in json.load(file)]
        except FileNotFoundError:
            return []

class CSVStorage(StorageStrategy):
    """Handles saving and loading tasks in CSV format."""
    
    def save(self, tasks, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
    
    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                return [Task(row["Task ID"], row["Title"], row["Description"], row["Due Date"], row["Status"]) for row in reader]
        except FileNotFoundError:
            return []

class ToDoApp:
    """Main application class for managing tasks."""
    
    def __init__(self, storage_strategy):
        self.tasks = []
        self.storage_strategy = storage_strategy
        self.load_tasks()
    
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)
    
    def update_task(self, task_id, title, description, due_date, status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                task.due_date = due_date
                task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")
    
    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with the given status.")
        else:
            for task in filtered_tasks:
                print(task)
    
    def save_tasks(self):
        self.storage_strategy.save(self.tasks, "tasks_data")
        print("Tasks saved successfully!")
    
    def load_tasks(self):
        self.tasks = self.storage_strategy.load("tasks_data")

# Example Usage
if __name__ == "__main__":
    storage = JSONStorage()  # Change to CSVStorage() for CSV format
    app = ToDoApp(storage)
    
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
        
        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ") or None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            app.add_task(Task(task_id, title, description, due_date, status))
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title: ")
            description = input("Enter new Description: ")
            due_date = input("Enter new Due Date (YYYY-MM-DD): ") or None
            status = input("Enter new Status (Pending/In Progress/Completed): ")
            app.update_task(task_id, title, description, due_date, status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            app.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            app.filter_tasks(status)
        elif choice == "6":
            app.save_tasks()
        elif choice == "7":
            app.load_tasks()
            print("Tasks loaded successfully!")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
