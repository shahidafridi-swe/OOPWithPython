class Animal:
    def __init__(self, name) -> None:
        self.name = name
        
    def speak(self):
        print(f"{self.name} is speaking")
        
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def speak(self):
        print(f"{self.name} is meowing meowing")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def speak(self):
        print(f"{self.name} is gheuing gheuing")

class Mouse(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
tom = Cat("Mr. Tomas")
bull = Dog("Mr. Bull Dog")
jerry = Mouse("Jerry")

tom.speak()
bull.speak()
jerry.speak()

        