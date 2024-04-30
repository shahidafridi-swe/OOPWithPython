from abc import ABC, abstractmethod
from order import Order
class User:
    def __init__(self, name, email, phone, address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Admin(User):
    def __init__(self, name, email, phone, address) -> None:
        super().__init__(name, email, phone, address)

    def add_employee(self,restaurent, employee):
        restaurent.add_employee(employee)

    def view_employees(self,restaurent):
        restaurent.view_employees()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self,restaurent,item_name):
        restaurent.menu.remove_item(item_name)
    
    def view_items(self, restaurent):
        restaurent.menu.show_menu()

        
class Customer(User):
    def __init__(self, name, email, phone, address) -> None:
        super().__init__(name, email, phone, address)
        self.cart = Order()
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if item.quantity > quantity:
                print(f"{item_name} added to cart")
                item.quantity = quantity
                self.cart.add_item(item)
            else:
                print("Item exeeded!!!")
        else:
            print(f"{item_name} not found")

    def view_cart(self):
        print("------- Cart List -------")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        
        print(f"Total Price : {self.cart.total_price} BDT")

    def pay_bill(self):
        print(f"{self.cart.total_price} BDT paid successfully!!!")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary) -> None:
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary



    