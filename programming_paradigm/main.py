# programming_paradigm/main.py

from bank_account import BankAccount

def main():
    account = BankAccount(250)

    account.withdraw(300)
    print(f"Current Balance: ${account.get_balance():.2f}")

if __name__ == "__main__":
    main()
