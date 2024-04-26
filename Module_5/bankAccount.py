class BankAccount:
    bankName = 'Bangladesh Bank' #class attribute
    
    #constructor
    def __init__(self, accountName, openningBalance =1000):
        #class attribute
        self.accountName = accountName
        #class attribute
        self.balance = openningBalance
        print(f"Dear {accountName}, Your account create succesfull in {self.bankName}.")
    
    def getBalance(self):
        print(f"Dear {self.accountName}, Your current balance is: {self.balance} BDT")
        return self.balance
    
    def deposit(self, amount): #methods
        if amount > 0:
            self.balance += amount
            print(f"Hello {self.accountName}, your {amount} BDT deposit successfull. Your current balance is: {self.balance} BDT.")
    
    def withdraw(self, amount): 
        if amount > 100000:
            print(f"{self.accountName}, You can't withdraw more than 100000 BDT in a single time")
        elif amount > self.balance:
            print(f"Sorry {self.accountName} !!! You have no sufficient balance to withdraw {amount} BDT \nYour current balance is: {self.balance} BDT")
        elif amount > 0 :
            self.balance -= amount
            print(f"{self.accountName}, Here is your {amount} BDT")
            print(f"After withdrawn your current balance now: {self.balance} BDT")   
        else:
            print("Please give the right amount to withdraw")
    
    
shahid = BankAccount("Shahid")
ruma = BankAccount("Ruma")

shahid.deposit(50000)
ruma.getBalance()
ruma.withdraw(500)
ruma.getBalance()
ruma.deposit(76730000)
ruma.getBalance()
shahid.getBalance()


    