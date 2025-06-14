class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance_file = "balance.txt"
        try:
            with open(self.balance_file, "r") as f:
                self.balance = float(f.read())
        except FileNotFoundError:
            self.balance = initial_balance
            self._save_balance()

    def _save_balance(self):
        with open(self.balance_file, "w") as f:
            f.write(str(self.balance))

    def deposit(self, amount):
        self.balance += amount
        self._save_balance()
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self._save_balance()
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
