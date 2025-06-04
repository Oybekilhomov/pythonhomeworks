
##Model a Farm
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Moo")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Cluck")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

class Pig(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Oink")

    def roll_in_mud(self):
        print(f"{self.name} is rolling in the mud.")

def farm_simulation():
    cow = Cow("Bessie", 5)
    chicken = Chicken("Clucky", 2)
    pig = Pig("Porky", 3)

    print("--- Cow ---")
    cow.eat()
    cow.make_sound()
    cow.produce_milk()

    print("\n--- Chicken ---")
    chicken.sleep()
    chicken.make_sound()
    chicken.lay_eggs()

    print("\n--- Pig ---")
    pig.eat()
    pig.make_sound()
    pig.roll_in_mud()

if __name__ == "__main__":
    farm_simulation()


##Build a Bank Application

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
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}.")
        else:
            print("Invalid withdrawal amount.")

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'name': self.name,
            'balance': self.balance
        }

    @staticmethod
    def from_dict(data):
        return Account(data['account_number'], data['name'], data['balance'])


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1).zfill(6)
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        print(f"Account created! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.accounts.items()}, f, indent=4)
        print("Accounts saved to file.")

    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                self.accounts = {k: Account.from_dict(v) for k, v in data.items()}
            print("Accounts loaded from file.")


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Save & Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, deposit)
        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.view_account(acc_num)
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_num, amount)
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_num, amount)
        elif choice == "5":
            bank.save_to_file()
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
