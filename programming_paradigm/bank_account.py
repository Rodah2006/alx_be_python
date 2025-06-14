

class BankAccount:
    def __init__(self, balance_file="balance.txt"):
        self.balance_file = balance_file
        try:
            with open(self.balance_file, "r") as f:
                self.account_balance = float(f.read())
        except (FileNotFoundError, ValueError):
            self.account_balance = 100  # default balance

    def deposit(self, amount):
        self.account_balance += amount
        self.save_balance()

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.save_balance()
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

    def save_balance(self):
        with open(self.balance_file, "w") as f:
            f.write(str(self.account_balance))
