from bank_account import *

john = BankAcct("John Doe", 1000)
sara = BankAcct("Sara Doe", 2000)

# john.deposit(500)
# john.withdraw(80)
# john.transfer(100, sara)

adam = InterestAcct("Adam Doe", 1000)
adam.deposit(500)
adam.withdraw(80)
adam.transfer(100, sara)

julie = SavingsAcct("Julie Doe", 1000)
julie.deposit(500)
julie.withdraw(80)
julie.transfer(100, sara)