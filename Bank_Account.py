"""
Exercise 1: Bank Account
Create a BankAccount class that represents a bank account.
The class should have the following attributes and methods:
Attributes:
account_number (string)
balance (float)
Methods:
deposit(amount): Adds the specified amount to the account balance.
withdraw(amount): Subtracts the specified amount from the account balance.
get_balance(): Returns the current account balance.
"""


class BancAccount:
    account_number = ""
    balance = 0.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter amount to deposited: "))
        if self.amount>0:
          self.balance +=amount
          return f"deposited {self.amount}, current balance after deposit is {self.balance}"
        else: return print("Unidentified digit")

    def withdraw(self):
        self.draw = float(input("Enter amount to withdraw: "))
        if self.balance >= self.draw + 20:
            self.balance = self.balance - self.draw
            return f"You have withdrawn {self.draw}"
        else:
            return f"Insufficient balance"

    def get_balance(self):
        return f"Your account balance is {self.balance}"


obj = BancAccount("02105210", 10)
depositing = obj.deposit()
print(depositing)
withdrawing = obj.withdraw()
print(withdrawing)
check_balance = obj.get_balance()
print(check_balance)
