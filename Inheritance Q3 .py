'''
Pillar 2: Inheritance
Q3. Employee Roles | Beginner
Create a parent class Employee that stores a name and employee ID and provides display_details(). Derive
Developer (programming language) and Manager (team size). Use super() to initialize inherited attributes.
Override display_details() in each child class to include both shared and role-specific information. Create and test
one object of each type.
'''
# Q3.py - Employee Roles

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id) # Parent ka data
        self.programming_language = programming_language

    def display_details(self):
        print(f"[Developer] Name: {self.name}, ID: {self.emp_id}, Language: {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def display_details(self):
        print(f"[Manager] Name: {self.name}, ID: {self.emp_id}, Team Size: {self.team_size}")

# --- Demo - 1 Object of each type ---
print("--- Testing ---")

dev1 = Developer("Ali", 101, "Python")
mgr1 = Manager("Sara", 201, 10)

dev1.display_details()
mgr1.display_details()

# Ek aur object extra
dev2 = Developer("Zain", 102, "JavaScript")
dev2.display_details()

