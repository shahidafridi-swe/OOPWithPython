class Shop:
    shopingMall = 'Basundhora'
    cart = []  # Here cart is class attribute
    
    def __init__(self, buyer):
        self.buyer = buyer
        
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