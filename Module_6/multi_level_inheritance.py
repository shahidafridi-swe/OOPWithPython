class Vehicle:
    def __init__(self, name, model, price, color) -> None:
        self.name = name
        self.model = model
        self.price = price
        self.color = color
        
    
    def __repr__(self) -> str:
        return f"Vehicle: {self.name}, Model: {self.model}, Price: {self.price} BDT"
    
    def run(self):
        pass
    
    
class Bus(Vehicle):
    
    def __init__(self, name, model, price, color, seat) -> None:
        self.seat = seat
        super().__init__(name, model, price, color)
        
    def __repr__(self) -> str:
        print(f"{self.name} Bus, Seat: {self.seat}")
        return super().__repr__()
    
class ACBus(Bus):
    def __init__(self, name, model, price, color, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(name, model, price, color, seat)
        
    def __repr__(self) -> str:
        print(f"Temperature: {self.temperature} Degree.")
        return super().__repr__()
    
greenLine = ACBus("Green Line", "GL2024AC", 76730000, "Green", 30,16)

print(greenLine)