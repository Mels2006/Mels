# Exercise: Bank Account Hierarchy
# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. Balance: ${self.balance}")
        
    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate=0.1):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        interest_earned = amount * self.interest_rate
        self.balance += interest_earned
        print(f"Interest earned: ${interest_earned}. Balance: ${self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_fee=30):
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"overdraft fee: ${self.overdraft_fee}")
            self.balance -= self.overdraft_fee

savings_account = SavingsAccount(account_number= " ", balance=1000)
savings_account.deposit(500)

checking_account = CheckingAccount(account_number= "  ", balance=1000)
checking_account.withdraw(1100)

print(f"Checking Account Balance: ${checking_account.get_balance()}")

