# Create SavingsAccount with id, customer, balance 
# create method to deposit, withdraw and get balance
# validate all inputs and raise exceptions if invalid

class SavingsAccount:
    """Simple savings account with deposit, withdraw, and balance inquiry."""

    def __init__(self, account_id, customer_name, balance=0):
        """Initialize a SavingsAccount.

        Args:
            account_id: Unique identifier for the account.
            customer_name: Name of the account owner.
            balance: Initial amount in the account. Defaults to 0.
        """
        self.account_id = account_id
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw a positive amount from the account if funds are sufficient."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        """Return the current account balance."""
        return self.balance
    

    
