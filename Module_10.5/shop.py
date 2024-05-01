from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

    @abstractmethod
    def view_all_products(self):
        pass

class Seller(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.type = 'admin'
        
    def add_product(self,shop, product):
        shop.menu.add_product(product)
    
    def view_all_products(self,shop):
        shop.menu.view_all_products()

    def remove_product(self,shop, product_name):
        shop.menu.remove_product(product_name)

    def update_product(self,shop, product_name):
        shop.menu.update_product(product_name)

class Order:
    def __init__(self) -> None:
        self.products = {}

    def add_product(self, product,quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self,product_name):
        for product in self.products.keys():
            if product.name == product_name:
                self.products.pop(product)
                print(f"\t{product_name} removed from cart !!!")
                return
        print(f"\t{product_name} not found in cart !!!")

    def clear_order(self):
        self.products = {}    
    



class Customer(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.type = 'customer'
        self.cart = Order()
    
    def view_all_products(self,shop):
        shop.menu.view_all_products()

    def add_to_cart(self,shop, product_name):
        isProduct =shop.menu.find_product(product_name)
        if isProduct:
            quantity = int(input(f"How many {isProduct.name} you want to buy: "))
            if 0< quantity <= isProduct.quantity:
                self.cart.add_product(isProduct,quantity)
                print(f"{quantity} pc {product_name} added into cart")
            else:
                print(f"Quantity have to must 1 to {isProduct.quantity}")
        else:
            print(f"Sorry ! {product_name} in not found")
    def view_cart(self):
        print(f"------- Your Cart -------")
        print("\tName\tPrice\tOrigin\tQuantity")
        print("-----------------------------------------------------------------------------")
        for product, quantity in self.cart.products.items():
            print(f"\t{product.name}\t{product.price}\t{product.origin}\t{quantity}")

    def remove_product_from_cart(self, product_name):
        self.cart.remove_product(product_name)

    def pay_bill(self):
        for product , quantity in self.cart.products.items():
            product.quantity -= quantity
        self.cart.clear_order()
        print("Bill paid successfully!!!")




class Product:
    def __init__(self, name, price, origin, quantity) -> None:
        self.name = name
        self.price = price 
        self.origin = origin
        self.quantity = quantity

    def update_product(self, name, price, origin, quantity):
        self.name = name
        self.price = price 
        self.origin = origin
        self.quantity = quantity

class Shop:
    def __init__(self, name, address) -> None:
        self.name = name 
        self.address = address
        self.menu = Menu()
        self.users = []

class Menu:
    def __init__(self) -> None:
        self.products = []

    
    def add_product(self, product):
        isProduct = self.find_product(product.name)
        if isProduct:
            print(f"\tSorry ! Your product added failed!!!\n\tAlready '{product.name}' name of product have in our shop, Try another name to add.")
        else:
            self.products.append(product)
            print(f"\tYour '{product.name}' name of product added succseefully!")

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None    
    
    def view_all_products(self):
        print("\n------- All Products -------")
        print("\tName\tPrice\tOrigin\tQuantity")
        print("-----------------------------------------------------------------------------")
        for product in self.products:
            print(f"\t{product.name}\t{product.price}\t{product.origin}\t{product.quantity}")
        
    def remove_product(self, product_name):
        isProduct = self.find_product(product_name)

        if isProduct:
            self.products.remove(isProduct)
            print(f"'{product_name}' removed successfully!")
        else:
            print(f"'{product_name}' not found.")
    
    def update_product(self, product_name):
        isProduct = self.find_product(product_name)

        if isProduct:
            print("Your selected product's current data:")
            print("\tName\tPrice\tOrigin\tQuantity")
            print("-----------------------------------------------------------------------------")
            print(f"\t{isProduct.name}\t{isProduct.price}\t{isProduct.origin}\t{isProduct.quantity}")

            name = input("Enter the updated name: ")
            price = float(input("Enter the updated price: "))
            quantity = int(input("Enter the updated quantity: "))
            origin = input("Enter the updated origin: ")
            isProduct.update_product(name, price, origin, quantity)
            print(f"{product_name} updated successfully!")
        else:
            print(f"{product_name} not found!")
            

aymanStore =Shop("Ayman Store", "Rajshahi")


while True:
    print(f"------- Welcome to {aymanStore.name} --------")

    print("Press 1 for seller")
    print("Press 2 for customer")
    print("Press 0 for customer")

    currentUser = None
    s_c = input("Press 1 / 2 : ")
    if s_c == '0':
        break
    
    elif s_c == '1':
        print("\n\tLogin / Resister (L/R) ?")
        opLogin = input("Please enter (L/R) : ") 

        if opLogin == 'R':
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            user = Seller(name, email,password)
            aymanStore.users.append(user)
            currentUser = user
        elif opLogin == 'L':
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            for user in aymanStore.users:
                if user.email == email and user.password == password and user.type == 'admin':
                    currentUser = user
                    break
            if not currentUser :
                print("Credential were wrong, Try Again !!!")
        if currentUser:
            print(f"Welcome {currentUser.name}")
            while True:
                print("Options:")
                print("1. Add Product")
                print("2. Update Product")
                print("3. Delete Product")
                print("4. View All Products")
                print("5. Log Out")

                op = input("Please Enter Your Choice: ")
                if op == '1':
                    name = input("Enter the product name: ")
                    price = float(input("Enter the product price: "))
                    origin = input("Enter the product origin: ")
                    quantity = int(input("Enter the product quantity: "))
                    product = Product(name,price,origin,quantity)
                    currentUser.add_product(aymanStore,product)
                elif op == '2' :
                    product_name = input("Entrer the product name: ")
                    currentUser.update_product(aymanStore,product_name)
                elif op == '3' :
                    product_name = input("Entrer the product name: ")
                    currentUser.remove_product(aymanStore,product_name)
                elif op == '4' :
                    currentUser.view_all_products(aymanStore)
                elif op == '5' :
                    currentUser = None
                    print("Logged Out")
                    break
                
    elif s_c == '2':
        print("\n\tLogin / Resister (L/R) ?")
        opLogin = input("Please enter (L/R) : ") 

        if opLogin == 'R':
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            user = Customer(name, email,password)
            aymanStore.users.append(user)
            currentUser = user
        elif opLogin == 'L':
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            for user in aymanStore.users:
                if user.email == email and user.password == password and user.type == 'customer':
                    currentUser = user
                    break
            if not currentUser :
                print("Credential were wrong, Try Again !!!")
        if currentUser:
            print(f"Welcome {currentUser.name}")
            while True:
                print("Options:")
                print("1. Add To Cart")
                print("2. View Cart")
                print("3. Remove Product From Cart")
                print("4. View All Products")
                print("5. Pay Bill")
                print("6. Log Out")

                op = input("Please Enter Your Choice: ")
                if op == '1':
                    product_name = input("Enter the product name: ")
                    currentUser.add_to_cart(aymanStore,product_name)
                elif op == '2' :
                    currentUser.view_cart()
                elif op == '3' :
                    product_name = input("Enter the product name: ")
                    currentUser.remove_product_from_cart(product_name)
                elif op == '4' :
                    currentUser.view_all_products(aymanStore)
                elif op == '5' :
                    currentUser.pay_bill()
                elif op == '6' :
                    currentUser = None
                    print("Logged Out")
                    break

