# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0, balance_file="balance.txt"):
        self.balance_file = balance_file
        self.balance = initial_balance

        try:
            with open(self.balance_file, "r") as f:
                self.balance = float(f.read())
        except FileNotFoundError:
            self._save_balance()
        except ValueError:
            print("Invalid balance value. Resetting to 0.")
            self.balance = 0
            self._save_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._save_balance()
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._save_balance()
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")  # ✅ ALX expects this line

    def _save_balance(self):
        with open(self.balance_file, "w") as f:
            f.write(str(self.balance))
