class Product:
    def __init__(self, name, productID, price) -> None:
        self.name = name
        self.productID = productID
        self.price = price
        
    def __repr__(self) -> str:
        return f"Product name: {self.name}, Price: {self.price}"
    
    
class Shop:
    def __init__(self,shopName) -> None:
        self.shopName = shopName
        self.products = []
        
    def add_product(self, productName,productID, price):
        product = Product(productName,productID,price)
        self.products.append(product)
    
    def all_products(self):
        for product in self.products:
            print(product)
        
    def buy_product(self, productName):
        for product in self.products:
            if product.name== productName:
                print(f"Congrates!!! Here is your {productName}")
                self.products.remove(product)
                return 
        print(f"Sorry !!! At this moment {productName} is not available in our shop")
        
aymazon = Shop('AymaZon')

aymazon.add_product("iPhone", "apple14", 120000)
aymazon.add_product("Laptop", "lptp420", 70000)
aymazon.add_product("Camera", "cnn24", 170000)


aymazon.buy_product("Laptop")
aymazon.buy_product("Laptop")
aymazon.buy_product("Watch")




        