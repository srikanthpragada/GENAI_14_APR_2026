# Create SavingsAccount with id, customer, balance 
# create method to deposit, withdraw and get balance
# validate all inputs and raise exceptions if invalid

class SavingsAccount:
    def __init__(self, account_id, customer_name, balance=0):
        self.account_id = account_id
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
    

    
