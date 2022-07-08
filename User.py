class User:
    accounts = []
    def __init__(self,name,email,balance = 0,interest_account = 0):
        self.name = name
        self.email = email
        self.bank_account = BankAccount(balance,interest_account)
        User.accounts.append(self.bank_account)
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return(self)
    def make_withdrawal(self,amount):
        self.account.withdrawal(amount)
        return(self)
    def show_user_balance(self):
        #print(self.name, BankAccount(self))
        self.account.show_account_info()
        #return(self)
    def transfer_money(self, other_user, amount):
        self.account.withdrawal(amount)
        other_user.account.deposit(amount)
        return(self)

user1 = User("Edwin","edwin@gmail.com",500,1)
user2 = User("Jack","jack@gmail.com")


user2.make_deposit(5000).make_withdrawal(4000).transfer_money(user1,500).show_user_balance()
user1.make_deposit(5000).make_withdrawal(4000).show_user_balance()