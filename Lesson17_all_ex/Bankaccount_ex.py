# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information.
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit is ${amount}")
        else:
            print(f"Deposit is not correct")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw is ${amount}")
        else:
            print(f"withdraw is not correct")
    def get_balance(self):
        return f"Balance of account_holder is ${self.balance}"       
account1 = BankAccount(account_holder = "Mels Sargsyan",balance = 1000)
account1.deposit(500)
account1.withdraw(200)
print(account1.get_balance())






