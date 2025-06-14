import sys
from bank_account import BankAccount

def main():
    account = BankAccount(250)  # Starting balance

    if len(sys.argv) != 2:
        print("Usage: python main.py [deposit:amount|withdraw:amount|display]")
        return

    action = sys.argv[1]

    if action.startswith("deposit:"):
        amount = float(action.split(":")[1])
        account.deposit(amount)

    elif action.startswith("withdraw:"):
        amount = float(action.split(":")[1])
        account.withdraw(amount)

    elif action == "display":
        account.display_balance()

    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()
