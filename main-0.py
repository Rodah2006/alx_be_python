import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py [display|deposit:<amount>|withdraw:<amount>]")
        return

    command = sys.argv[1]

    if command == "display":
        account.display_balance()
    elif command.startswith("deposit:"):
        try:
            amount = float(command.split(":")[1])
            account.deposit(amount)
        except ValueError:
            print("Invalid amount.")
    elif command.startswith("withdraw:"):
        try:
            amount = float(command.split(":")[1])
            account.withdraw(amount)
        except ValueError:
            print("Invalid amount.")
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
