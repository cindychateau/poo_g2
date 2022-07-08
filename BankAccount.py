class BankAccount:
    bank = "First National DOJO"
    all_accounts = []
    def __init__(self,balance, interest_rate):
        self.account_balance = balance
        self.interest_rate = interest_rate/100
        BankAccount.all_accounts.append(self)
    def deposit(self,amount):
        self.account_balance += amount
        return self
    def withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def show_account_info(self):
        print(f"Balance: {self.account_balance}")
    def generate_rate(self):
        if self.account_balance > 0:
            self.account_balance *= (1 + self.interest_rate)
            return self
    @classmethod
    def show_instances(cls):
            print(cls.all_accounts)
            print(cls.bank)