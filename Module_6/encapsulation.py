#  Encapsulation --> Hide information
#  Access Modifier : Public, Private, Protected

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name #Public Attribute
        self.__balance = initial_deposit #Private Attribute
        self._branch = "Banani" #Protected Attribute
        
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance +=amount
        
shahid = Bank("Shahid Afridi", 10000)

print(shahid.getBalance())


# Show Private value
# print(dir(shahid))
# print(shahid._Bank__balance)
    