class BankAccount:
    def __init__(self, initial_balance):
        self.balance_file = "balance.txt"

        try:
            with open(self.balance_file, "r") as f:
                self.balance = float(f.read())
        except (FileNotFoundError, ValueError):
            # If file doesn't exist or content is bad, use initial balance
            self.balance = float(initial_balance)
            self._save_balance()

    def _save_balance(self):
        with open(self.balance_file, "w") as f:
            f.write(f"{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self._save_balance()
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self._save_balance()
            print(f"Withdrew: ${amount}")

    def display(self):
        print(f"Current Balance: ${self.balance:.2f}")
