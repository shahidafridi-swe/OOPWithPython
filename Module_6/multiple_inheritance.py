class Person:
    def __init__(self, name, NID) -> None:
        self.name = name
        self.NID = NID
        
    def __repr__(self) -> str:
        return f"Name: {self.name}, NID: {self.NID}"

class Family:
    def __init__(self, member) -> None:
        self.member = member

class Sports:
    def __init__(self, game) -> None:
        self.game = game
        

class Student(Person, Family, Sports):
    def __init__(self, name, NID, member, game) -> None:
        Person.__init__(self, name,NID)
        Family.__init__(self, 7)
        Sports.__init__(self, "Cricket")
        
        
    def __repr__(self) -> str:
        print(f"{self.name}, game: {self.game}")
        return super().__repr__()    
    

shahid = Student('Shahid Afridi', 8702052856, 7, "Cricket")

print(shahid)