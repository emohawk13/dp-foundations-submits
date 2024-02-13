class BankATM:
    def __init__(self):
        self.balance = 0.0

    def check_balance(self):
        return f"Your balance is ${self.balance:.2f}"

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                return f"You have deposited ${amount:.2f}"
            else:
                return "Invalid deposit amount."
        except ValueError:
            return "Invalid input. Please enter a number."

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    return f"Please take your ${amount:.2f}. Your balance is now ${self.balance:.2f}"
                else:
                    return f"This amount exceeds your balance of ${self.balance:.2f}"
            else:
                return "Invalid withdrawal amount."
        except ValueError:
            return "Invalid input. Please enter a number."

def main():
    atm = BankATM()
    print("Hello and Welcome to the Bank of Dauhson")

    while True:
        print("\nPlease select from the following menu options:")
        print("(B)alance")
        print("(D)eposit")
        print("(W)ithdraw")
        print("(Q)uit")
        choice = input().strip().lower()

        if choice == 'b':
            print(atm.check_balance())
        elif choice == 'd':
            deposit_amount = input("How Much Would You Like to Deposit? $")
            print(atm.deposit(deposit_amount))
        elif choice == 'w':
            withdraw_amount = input("How much would you like to withdraw? (0 to cancel): $")
            if withdraw_amount == '0':
                continue
            print(atm.withdraw(withdraw_amount))
        elif choice == 'q':
            print("Goodbye. Please come again")
            break
        else:
            print("Invalid choice. Please select a valid option \n B for Balance, D for Deposit, W for Withdraw, and Q to quit using the ATM.")

if __name__ == "__main__":
    main()
