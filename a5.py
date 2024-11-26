
import re
class Account:
    bank_name = "State Bank of India"
    currency = "INR"
    minimum_balance = 3000

    def __init__(self, account_number, holder_name, account_type, initial_balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = initial_balance

        if self.balance < Account.minimum_balance:
            raise ValueError(f"Initial balance must be at least {Account.minimum_balance} {Account.currency}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): 
        if amount <= 0:
            return False
        if self.balance - amount >= Account.minimum_balance:
            self.balance -= amount
            return True
        return False

    def balance_enquiry(self):
        return self.balance

    def display_details(self):
        return {
            "Account Number": self.account_number,
            "Holder Name": self.holder_name,
            "Account Type": self.account_type,
            "Balance": f"{self.balance:.2f} {Account.currency}",
            "Bank Name": Account.bank_name
        }

def is_valid(value):
    return value.replace('.', '', 1).isdigit() and len(value) > 0

def main():
        while True:
            acc_number = input("Enter  account number: ")
            if len(acc_number) == 10 and acc_number.isdigit():
                break
            else:
                print("Invalid account number. Please enter a 10-digit number.")

        while True:
            holder_name = input("Enter account holder name: ")
            if re.match("^[A-Za-z\s\.'']+$", holder_name):
                break
            else:
                print("Invalid name. Please enter only alphabetic characters.")
            
        while True:
            acc_type = input("Enter account type (saving/current): ").lower()
            if acc_type in ["saving", "current"]:
                break
            else:
                print("Invalid account type. Please enter either 'saving' or 'current'.")

        while True:
            initial_balance_input = input(f"Enter initial balance (minimum {Account.minimum_balance} {Account.currency}): ")
            if is_valid(initial_balance_input):
                initial_balance = float(initial_balance_input)
                if initial_balance >= Account.minimum_balance:
                    break
                else:
                    print(f"Initial balance must be at least {Account.minimum_balance} {Account.currency}.")
            else:
                print(" Invalid input. Please enter a valid numeric value.")

        account = Account(acc_number, holder_name, acc_type, initial_balance)

        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Balance Enquiry\n4. Display Account Details\n5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                amount = input("Enter amount to deposit: ")
                if is_valid(amount):
                    if account.deposit(float(amount)):
                        print("Deposit successful.")
                    else:
                        print("Deposit amount must be positive.")
                else:
                    print("Invalid amount. Please enter a valid numeric value.")
            elif choice == "2":
                amount = input("Enter amount to withdraw: ")
                if is_valid(amount):
                    if account.withdraw(float(amount)):
                        print("Withdrawal successful.")
                    else:
                        print("Cannot withdraw. Minimum balance required.")
                else:
                    print("Invalid amount. Please enter a valid numeric value.")
            elif choice == "3":
                balance = account.balance_enquiry()
                print(f"Current balance: {balance:.2f} {Account.currency}")
            elif choice == "4":
                details = account.display_details()
                for key, value in details.items():
                    print(f"{key}: {value}")
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid option. Try again.")
main()
