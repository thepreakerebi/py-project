class BalanceException(Exception):
    pass

class BankAcct:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Welcome {self.name}, your balance is ${self.balance}")
    
    def get_balance(self):
        print(f"Your balance is ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited ${amount}")
        self.get_balance()

    def viable_withdrawal(self, amount):
        if amount >= self.balance:
            raise BalanceException("You can't withdraw more than what you have in your account")
        else:
            self.balance -= amount
            print(f"You have withdrawn ${amount}")
            self.get_balance()
    
    def withdraw(self, amount):
        try:
            self.viable_withdrawal(amount)
        except BalanceException as e:
            print(f"Withdrawal failed. {e}")

    def transfer(self, amount, other_acct):
        try:
            self.viable_withdrawal(amount)
            other_acct.deposit(amount)
        except BalanceException as e:
            print(f"Transfer failed. {e}")

class InterestAcct(BankAcct):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        print(f"Your interest account has been created. You have ${self.balance} in it.")

    def deposit(self, amount):
        self.balance += amount * 1.01
        print(f"You have deposited ${amount}")
        self.get_balance()



class SavingsAcct(InterestAcct):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        print(f"Your savings account has been created. You have ${self.balance} in it.")
    
    def withdraw(self, amount):
        try:
            self.viable_withdrawal(amount)
        except BalanceException as e:
            print(f"Withdrawal failed. {e}")