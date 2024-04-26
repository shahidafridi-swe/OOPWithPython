class Bank:
    
    def __init__(self, balance):
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount} BDT deposit successfull. \nNow Your Balance: {self.getBalance()} BDT')
        else :
            print("Please give the right amount to deposit")
            
        
    def withdraw(self, amount):
        if amount > 100000:
            print("You can't withdraw more than 100000 BDT in a single time")
        elif amount > self.balance:
            print(f"You have no sufficient balance to withdraw {amount} BDT \nYour current balance is: {self.balance} BDT")
        elif amount > 0 :
            self.balance -= amount
            print(f"Here is your {amount} BDT")
            print(f"After withdrawn your current balance now: {self.balance}")   
        else:
            print("Please give the right amount to withdraw")
        
grameen = Bank(50000)

print(grameen.getBalance(),"BDT")

grameen.deposit(10000)
grameen.withdraw(1000)

