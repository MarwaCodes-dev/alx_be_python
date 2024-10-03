class BankAccount:
    def __init__(self,account_balance) :
        self.account_balance= account_balance
    def deposit(self,amount) : 
        self.amount += account_balance
    def withdraw(self,amount) :
        self.amount -= account_balance
        if account_balance>amount:
            return True
        else:
            return False

    def display_balance(self) :
        print(f"Current Balance: ${amount}")
