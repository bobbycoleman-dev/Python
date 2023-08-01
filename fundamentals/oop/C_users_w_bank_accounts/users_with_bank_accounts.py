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

    def display_account_info(self, user_name, account_type):
        if account_type == "checking":
            print(f"{user_name}'s Checking Balance: ${self.balance}")
        else:
            print(f"{user_name}'s Savings Balance: ${self.balance}")

        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = round(((self.balance * self.int_rate) + self.balance), 2)
            return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking_account = BankAccount(int_rate=0.02, balance=0)
        self.has_savings_account = False

    def add_savings_account(self):
        self.savings_account = BankAccount(int_rate=0.02, balance=0)
        self.has_savings_account = True

    def make_deposit(self, amount, account_type):
        if account_type == "checking":
            self.checking_account.balance += amount
            return self
        elif account_type == "savings":
            self.savings_account.balance += amount
            return self

    def make_withdraw(self, amount, account_type):
        if account_type == "checking":
            self.checking_account.withdraw(amount)
            return self
        elif account_type == "savings":
            self.savings_account.withdraw(amount)
            return self

    def display_user_balance(self):
        self.checking_account.display_account_info(self.name, "checking")
        if self.has_savings_account:
            self.savings_account.display_account_info(self.name, "savings")
        return self

    def transfer_money(self, amount, other_user):
        self.checking_account.balance -= amount
        other_user.checking_account.balance += amount


user1 = User("Bobby", "bobby@email.com")
user1.add_savings_account()

user1.make_deposit(1500, "checking").make_deposit(500, "savings")
user1.make_withdraw(500, "checking").make_withdraw(250, "savings")

user2 = User("Joe", "mulletsrcool@hotrod.com")
user1.transfer_money(100, user2)
user1.display_user_balance()
user2.display_user_balance()
