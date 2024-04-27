from abc import ABC, abstractmethod
#abc -> Abstract Base Class
class Animal(ABC):
    
    @abstractmethod #Enforce all derived class to have a eat method
    def eat(self):
        print("I need food")
        
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = "Monkey"
        self.name = name
        super().__init__()
        
    def eat(self):
        print(f"{self.name} eats Banana")

class Cat(Animal):
    def __init__(self,name, color) -> None:
        self.category = "cat"
        self.name = name
        self.color = color
        super().__init__()

    def eat(self):
        print(f"{self.name} eats Milk")
   
hula = Monkey("Hula")
tom = Cat("Tom", "Black")


hula.eat()
tom.eat()
