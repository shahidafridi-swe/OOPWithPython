from users import User, Admin, Customer, Employee
from restaurent import Restaurent
from order import Order
from menu import Menu
from food_item import FoodItem

AFC = Restaurent('Ayman Food Center')

def customer_menu():
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    phone = input("Please enter your phone: ")
    address = input("Please enter your address: ")
    customer = Customer(name,email,phone,address)

    while True:
        print(f"------- Welcome {name} -------")
        print("1. View Menu")
        print("2. Add Item To Cart")
        print("3. View Cart ")
        print("4. Pay Bill")
        print("5. Exit")

        op = input("Enter your choice: ")

        if op == '1':
            customer.view_menu(AFC)
        elif op == '2':
            item_name = input("Please Enter Item Name: ")
            item_qauntity = int(input("Enter the quantity: "))
            customer.add_to_cart(AFC,item_name,item_qauntity)
        elif op == '3' :
            customer.view_cart()
        elif op == '4':
            customer.pay_bill()
        elif op == '5':
            break
        else:
            print("Invalid Input")
        

def admin_menu():
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    phone = input("Please enter your phone: ")
    address = input("Please enter your address: ")
    admin = Admin(name,email,phone,address)

    while True:
        print(f"------- Welcome {name} -------")
        print("1. Add Item")
        print("2. View Item")
        print("3. Delete Item")
        print("4. Add Employee")
        print("5. View Employee")
        print("6. Exit")

        op = input("Enter your choice: ")

        if op == '1':
            item_name = input("Enter the name of item: ")
            price = float(input("Enter the price for each quantity: "))
            quantity = int(input("Enter the item quantity: "))
            item = FoodItem(item_name, price,quantity)
            admin.add_new_item(AFC,item)
        elif op == '2':
            admin.view_items(AFC)
        elif op == '3' :
            item_name = input("Enter item name: ")
            admin.remove_item(AFC,item_name)
        elif op == '4':
            name = input("Enter employee name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            address = input("Enter address: ")
            age = input("Enter age: ")
            designation = input("Enter designation: ")
            salary = input("Enter salary: ")
            employee = Employee( name, email, phone, address, age, designation, salary)
            admin.add_employee(AFC,employee)
        elif op == '5':
            admin.view_employees(AFC)
        elif op == '6':
            break
        else:
            print("Invalid Input")
        

while True:
    print(f"------- Welcome to {AFC.name} -------")
    print("________________________________________")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    op = input("Enter Your Choice: ")
    if op == '1':
        customer_menu()
    elif op == '2':
        admin_menu()
    elif op == '3':
        break
    else:
        print("Invalid Input")











# admin.add_employee('Ruma', "ruma@gmail.com", "01704805887", "Rajshahi", 26, "Manager", 90000)

# AFC = Restaurent("Ayman Food Corner")
# admin = Admin('Shahid', 'shahidafridi@gmail.com', "01704805886", "Rajshahi")

# mn = Menu()
# pizza = FoodItem('Pizza', 75, 30)
# burger = FoodItem('Burger', 99, 15)
# admin.add_new_item(AFC,pizza)
# admin.add_new_item(AFC,burger)

# customer = Customer('Ayman', 'ayman@gmail.com','01558988666', "Rajshahi")
# customer.view_menu(AFC)

# item_name = input("Enter item name: ")
# item_qauntity = int(input("Enter item quantity: "))

# customer.add_to_cart(AFC,item_name, item_qauntity)
# customer.view_cart()