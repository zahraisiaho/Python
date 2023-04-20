class BankAccount:
    balance = 70000000

    def deposit(self):
        print("Deposit here")
    def withdraw(self):
        print("Withdraw here")
    def checkbalance(self):
        print("Check balance here")
    def transfer(self):
        print("Transfer here")

class InterestAccount(BankAccount):
    interest = "Nine percent interest rate"

    def depo(self):
        print("Enter deposit for interest here")

class ChargingAccount(BankAccount):
    fee = 1500

    def withdraw(self):
        print("Enter withdrawal charge here")

bank = InterestAccount()
bank.deposit()
bank.withdraw()
bank.checkbalance()
bal = bank.balance
print(bal)
irt = bank.interest
print(irt)
bank.depo()

bnk = ChargingAccount()
bnk.withdraw()
f = bnk.fee
print(f)





