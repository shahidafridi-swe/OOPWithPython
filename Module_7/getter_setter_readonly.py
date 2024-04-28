class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age
    
    # getter
    @property
    def salary(self):
        return self.__money
    
    #setter
    @salary.setter
    def salary(self,value):
        if value < 0:
            return "Give a positive amount"
        self.__money = value
    
samsu = User("Copa Samsu", 21, 15000)

# print(samsu.age()) # now age is an attribute
print(samsu.age)
print(samsu.salary)
samsu.salary= 5000
print(samsu.salary)
