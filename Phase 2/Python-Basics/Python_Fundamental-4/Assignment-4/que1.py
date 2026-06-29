# Logic:
# 1. Create BankAccount class
# 2. Store account details using constructor
# 3. Create deposit, withdraw and balance methods
# 4. Create object and call methods

class BankAccount:

    # Constructor
    def __init__(self, account_number, owner_name, balance):

        # Account details store kiye
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    # Deposit method use kiya balance update karne ke liye
    def deposit(self, amount):

        # Balance update kiya 
        self.balance += amount

        print(amount, "rupees deposited successfully")

    # Withdraw method
    def withdraw(self, amount):

        # Balance check kiya
        if amount <= self.balance:

            # Balance reduce kiya
            self.balance -= amount

            print(amount, "rupees withdrawn successfully")

        else:
            print("Insufficient balance")

    # Balance check method
    def check_balance(self):

        print("Current Balance =", self.balance)


# Object create kiya
acc1 = BankAccount(101, "Pritish", 5000)

# Methods call kiye
acc1.deposit(3000)
acc1.withdraw(1000)
acc1.check_balance()


# Q1:Create a class BankAccount with attributes:
# account_number, owner_name, balance
# Add methods deposit(), withdraw() and check_balance()