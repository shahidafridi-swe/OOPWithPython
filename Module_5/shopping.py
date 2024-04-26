class Shopping:
    
    def __init__(self, name):
        self.buyerName = name
        self.cart = []
        
    
    def addToCart(self, productName, price, quantity):
        product = {'productName':productName, 'price':price, 'quantity':quantity}
        self.cart.append(product) 
        
    def removeItem(self, removeItemName):
        for item in self.cart:
            if item['productName'] == removeItemName:
                self.cart.pop(self.cart.index(item))
        
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        
        if amount < total:
            print(f"Dear {self.buyerName}, Your bill is {total} BDT. You have to pay {total-amount} BDT more.")
        
        else:
            items = []
            for item in self.cart:
                items.append(item['productName'])
            print(f"Here is your {items} and extra {amount-total} BDT")
            
ruma = Shopping("Ruma")

ruma.addToCart("Borkha", 2500, 2)
ruma.addToCart("Shoe", 1800, 2)
ruma.addToCart("Sharee", 5200, 5)

ruma.removeItem("Shoe")

ruma.checkout(40000)
