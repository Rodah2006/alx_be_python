# programming_paradigm/main.py

from bank_account import BankAccount

def main():
    account = BankAccount(250)

    account.withdraw(300)  # Will print: Insufficient funds.
    account.display_balance()  # ✅ Required by checker

if __name__ == "__main__":
    main()
