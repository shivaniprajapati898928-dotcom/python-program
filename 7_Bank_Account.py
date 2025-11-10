# Define a class BankAccount with attributes like account number, name, and balance. Implement methods for deposit, withdrawal, and displaying account information

# Define the BankAccount class
class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    # Display account information
    def display_info(self):
        print("\n----- Account Information -----")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: ₹{self.balance:.2f}")
        print("--------------------------------")


# Example usage
account1 = BankAccount("SB101", "Sumit Kumar", 5000)

account1.display_info()
account1.deposit(1500)
account1.withdraw(2000)
account1.display_info()
