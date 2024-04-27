#  base class, parent class, common attribute + functionality class
#  derived class, child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self,brand,model, color, price) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        
    def run(self):
        pass


class Laptop:    
    def __init__(self,brand,model, color, price, memory) -> None:
        self.memory = memory
        super().__init__(brand,model, color, price)
        
    def coding(self):
        print("I am coding now")
        
    
class Phone(Gadget):
    def __init__(self,brand,model, color, price, camera) -> None:
        self.camera = camera
        super().__init__(brand,model, color, price)
        
    def call(self):
        print("Calling someone...")
    
    def __repr__(self) -> str:
        return f"Phone Name: {self.brand} {self.model}"  

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
    
    def cupture(self):
        print("Farhan is cupturing the photo")
        
        
# myPhone = Phone('12MP')
myPhone = Phone("Redmi","Note 9 Pro", "Sea Grean", 28990, "64MP")

print(myPhone)