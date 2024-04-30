from menu import Menu

class Restaurent:
    def __init__(self,name) -> None:
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f"Employee : {employee.name} added successfully!!!")
    
    def view_employees(self):
        print("------- Employe list -------")
        print("Name \t Email \t\t Phone \t\t Address")
        for emp in self.employees:
            print(f"{emp.name} \t {emp.email}  {emp.phone} \t {emp.address}")
