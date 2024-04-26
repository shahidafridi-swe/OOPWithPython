class Calculator:
    brand = "Casio"
    
    def add(self, *num): #methods
        sum = 0
        for i in num:
            sum += i
        return sum
    
    def deduct(self, num1, num2): #methods
        return num1 - num2

    def multiply(self, num1, num2): #methods
        return num1*num2
    
    def devide(self, num1, num2): #methods
        return num1/num2

print(Calculator().add(1,2,3))
print(Calculator().deduct(3,1))
print(Calculator().multiply(2,4))
print(Calculator().devide(15,3))