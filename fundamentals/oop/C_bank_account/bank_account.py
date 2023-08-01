class BankAccount:
    all_accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}")

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = round(((self.balance * self.int_rate) + self.balance), 2)
            return self


user1 = BankAccount()
user2 = BankAccount()

user1.deposit(200).deposit(100.50).deposit(100.25).withdraw(300).yield_interest()
user2.deposit(523.75).deposit(257.23).withdraw(150).withdraw(150).withdraw(
    250
).withdraw(100).yield_interest()

BankAccount.display_all_accounts()
