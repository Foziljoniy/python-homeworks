import os

class Employee:
    """Represents an individual employee."""
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        """Returns a string representation of the employee details."""
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    """Manages employee records with file handling."""
    FILE_NAME = "employees.txt"

    def __init__(self):
        # Ensure the file exists
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w"): pass

    def add_employee(self, employee):
        """Adds a new employee to the file."""
        if self.is_employee_id_unique(employee.employee_id):
            with open(self.FILE_NAME, "a") as file:
                file.write(str(employee) + "\n")
            print("Employee added successfully!")
        else:
            print("Error: Employee ID already exists!")

    def view_all_employees(self):
        """Displays all employee records."""
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
        
        if not records:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for record in records:
                print(record.strip())

    def search_employee(self, employee_id):
        """Searches for an employee by Employee ID."""
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print("Employee not found.")

    def update_employee(self, employee_id, new_name, new_position, new_salary):
        """Updates an employee's information in the file."""
        updated = False
        records = []
        
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    records.append(f"{employee_id}, {new_name}, {new_position}, {new_salary}\n")
                    updated = True
                else:
                    records.append(line)
        
        with open(self.FILE_NAME, "w") as file:
            file.writelines(records)
        
        if updated:
            print("Employee record updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self, employee_id):
        """Deletes an employee record from the file."""
        records = []
        deleted = False
        
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    deleted = True
                else:
                    records.append(line)
        
        with open(self.FILE_NAME, "w") as file:
            file.writelines(records)
        
        if deleted:
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")

    def is_employee_id_unique(self, employee_id):
        """Checks if an Employee ID is unique."""
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    return False
        return True

    def display_menu(self):
        """Displays the menu and handles user choices."""
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
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                employee = Employee(employee_id, name, position, salary)
                self.add_employee(employee)
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                new_name = input("Enter new Name: ")
                new_position = input("Enter new Position: ")
                new_salary = input("Enter new Salary: ")
                self.update_employee(employee_id, new_name, new_position, new_salary)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.display_menu()
