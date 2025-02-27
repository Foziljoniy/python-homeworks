import json
import os

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount} successfully. New balance: {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount} successfully. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds."

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1).zfill(6)  # Generates a unique 6-digit account number
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created successfully! Account Number: {account_number}"

    def view_account(self, account_number):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            return f"Account Number: {acc.account_number}\nName: {acc.name}\nBalance: {acc.balance}"
        return "Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, f)

    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                self.accounts = {acc: Account(**data[acc]) for acc in data}


# Example Usage
if __name__ == "__main__":
    bank = Bank()
    print(bank.create_account("John Doe", 1000))
    print(bank.view_account("000001"))
    print(bank.deposit("000001", 500))
    print(bank.withdraw("000001", 300))
    print(bank.view_account("000001"))