from bank_account import BankAccount

def main():
    account = BankAccount(250)

    if account.withdraw(300):
        print("Withdrew: $300")
    else:
        print("Insufficient funds.")

    account.display_balance()

if __name__ == "__main__":
    main()
