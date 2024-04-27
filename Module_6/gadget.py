class Laptop:
    
    def __init__(self, brand,model, color, price, memory) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.memory = memory
        
    def run(self):
        pass
    
    def coding(self):
        print("I am coding now")
        
    
class Phone:
    def __init__(self, brand,model, color, price, camera) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.camera = camera
        
    def run(self):
        pass
    
    def call(self):
        print("Calling someone...")
        

class Camera:
    def __init__(self, brand,model, color, price, pixel) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.pixel = pixel
        
    def run(self):
        pass
    
    def cupture(self):
        print("Farhan is cupturing the photo")
        