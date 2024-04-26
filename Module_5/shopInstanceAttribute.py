class Shop:
    shopingMall = 'Basundhora'
    
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # Here cart is instance attribute
        
        
    def addToCart(self, item):
        self.cart.append(item)


shahid = Shop('Shahid Afridi')
shahid.addToCart('Laptop')
shahid.addToCart('Mobile')
print(shahid.cart)


ruma = Shop('Ruma Bibi')
ruma.addToCart('Shoe')
ruma.addToCart('Borkha')
print(ruma.cart)