class Shopping:
    cart = [] # Class Attribute / Static Attribute
    origin = 'China' # Class Attribute / Static Attribute
    
    def __init__(self, name, location) -> None:
        self.name = name # Instance Attribute 
        self.location = location # Instance Attribute 
        
    def purcahse(self, item, price, amount):
        remaining = amount - price
        print(f"Buying: {item} for price: {price} and remaining: {remaining}")
    
    @staticmethod
    def multiply(a,b): #no need to use self in static method as parameter
        print(a*b)


    @classmethod
    def hudai_dekhi(self, item):
        print(f"Hudai {item} dekhi r ac er hawa khai")
        
        
# Shopping.purcahse(2,5,6)  # it give erorr
# Shopping.purcahse('abc',2,5,6) # abc for self , abc can be anything


jamuna = Shopping("Jamuna", "Jamuna Jam Special")
jamuna.purcahse(2,3,4,)

Shopping.hudai_dekhi("Phone") # using class method

# using static method
Shopping.multiply(3,6)
# jamuna.multiply(2,3)