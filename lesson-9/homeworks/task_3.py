import json
import csv

def load_tasks(filename):
    """Loads tasks from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def display_tasks(tasks):
    """Displays all tasks with ID, Task Name, Completed Status, and Priority."""
    print("ID | Task Name        | Completed | Priority")
    print("------------------------------------------------")
    for task in tasks:
        print(f"{task['id']}  | {task['task']} | {task['completed']} | {task['priority']}")

def save_tasks(filename, tasks):
    """Saves modified tasks back to the JSON file."""
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def calculate_stats(tasks):
    """Calculates task statistics: total, completed, pending, and average priority."""
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {round(avg_priority, 2)}")

def convert_to_csv(json_filename, csv_filename):
    """Converts tasks JSON file to a CSV file."""
    tasks = load_tasks(json_filename)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
    print(f"Tasks converted to {csv_filename}")

# Main program
task_file = 'tasks.json'
csv_file = 'tasks.csv'

tasks = load_tasks(task_file)
display_tasks(tasks)
calculate_stats(tasks)
convert_to_csv(task_file, csv_file)
