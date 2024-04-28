class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print("vat, poloa, mangso, roast, kacchi biriyani")
        
    def exercise(self):
        raise NotImplementedError
        
class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # Method overriding
    def eat(self):
        print("Only vegetables")
        
    # Method Overriding
    def exercise(self):
        print("Hvae to go to gym everyday")
        
    # Dunder method / magic method
    # + sign operator overload
    def __add__(self,other)  :
        return self.age + other.age
    
    # * sign operator overload
    def __mul__(self, other)  :
        return self.height * other.height
    
    # > sign operator overload
    def __gt__(self,other):
        return self.age > other.age
    
    
shahid = Cricketer("Shahid Afridi", 27,68,72,"BD")
ayman = Cricketer("Ayman Afridi", 5,30,20,"BD")

shahid.eat()
shahid.exercise()

print(shahid+ayman)
print(shahid*ayman)
print(shahid > ayman)