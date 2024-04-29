class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __gt__(self,other):
        return self.age > other.age
    


class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

lst =[]

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

lst.append(sakib)
lst.append(musfiq)
lst.append(kamal)
lst.append(jack)
lst.append(kalam)

mostAge=0
x = None
for item in lst:
    if(item.age > mostAge):
        mostAge = item.age
        x = item

print(x.name)