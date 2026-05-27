class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance#private attribute
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, newBalance):#setter method
            self.__balance = newBalance

acc1 = BankAccount("Pritish", 100_000)
acc1.set_balance(150_000)
print(acc1.name,acc1.get_balance())