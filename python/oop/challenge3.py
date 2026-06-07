class BankAccount:
    num_accounts = 0
    interest_rate = 0.02

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = int(balance)
        BankAccount.num_accounts += 1

    def add_interest(self):                 # regular
        self.balance += (self.balance * BankAccount.interest_rate)

    @classmethod
    def set_interest(cls, rate):            # class
        cls.interest_rate = rate

    @staticmethod
    def is_valid_amount(amount):            # static
        return amount > 0

# YOUR TASK — fill in below:
#  → create 2 accounts
account1 = BankAccount("Tejas Dutt", "25000")
account2 = BankAccount("Monkey D. Luffy", "1125000")



#  → print BankAccount.num_accounts
print(BankAccount.num_accounts) #>>2

#  → set_interest(0.05) via the classmethod
BankAccount.set_interest(0.05)
#  → add_interest to one account, print new balance


account2.add_interest()

print(account2.balance)

#  → test is_valid_amount(-50) and is_valid_amount(100)
print(BankAccount.is_valid_amount(-50))
print(BankAccount.is_valid_amount(100))