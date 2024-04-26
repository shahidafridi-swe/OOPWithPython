class Phone:
    manufactured = "China"
    
    #Constructor
    def __init__(self, owner, brand, price): #Constructor
        self.owner = owner
        self.brand = brand
        self.price = price
        
    
    def call(self):
        print("Calling Ruma...")
        
myphone = Phone('Shahid Afridi', 'Nokia', 5000)
print(myphone.owner, myphone.brand, myphone.price)

herPhone = Phone('Ruma', 'iPhone', 120000)
print(herPhone.owner, herPhone.brand, herPhone.price)


class Pen:
    manufactured = 'Bangladesh'
    
    #Constructor
    def __init__(self, brand, type, color, price): #Constructor
        self.brand = brand
        self.type = type
        self.color = color
        self.price = price
        
econoPen = Pen('Econo', 'Ballpen', 'Black', 5)
print(econoPen.brand, econoPen.type, econoPen.color, econoPen.price)

matadorPen = Pen('Matador', 'Gelpen', 'Red', 10)
print(matadorPen.brand, matadorPen.type, matadorPen.color, matadorPen.price)