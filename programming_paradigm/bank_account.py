class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False  # No print here!

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
