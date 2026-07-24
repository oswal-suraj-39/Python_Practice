# Define a class Employee having members id, name, department, salary. 
# Create a subclass called manager with member bonus. 
# Define methods accept and display in both the classes. 
# Create n objects of the manager class and 
# display the details of the manager having the maximum total salary (salary+bonus).

class Employee:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.department = ""
        self.salary = 0

    def accept(self):
        self.id = int(input("Enter employee id: "))
        self.name = input("Enter employee name: ")
        self.department = input("Enter department name: ")
        self.salary = int(input("Enter salary: "))

    def display(self):
        print("----- Employee Details -----")
        print("Employee ID: ",self.id)
        print("Employee Name: ",self.name)
        print("Department Name: ",self.department)
        print("Salary: ",self.salary)
        
class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.bonus = 0

    def accept(self):
        super().accept()
        self.bonus = int(input("Enter bonus: "))

    def display(self):
        super().display()
        print("Bonus: ",self.bonus)
        print("Total Salary: ",self.salary + self.bonus)
        
n = int(input("enter number of managers: "))
managers = []
total_salary = []

for i in range(n):
    print(f"\n----- Enter details for manager {i+1} -----")
    manager = Manager()
    manager.accept()
    managers.append(manager)
    total_salary.append(manager.salary + manager.bonus)