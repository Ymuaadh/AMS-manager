from models.Account import Account
import datetime

class Overdraft:
    def __init__(self, account: Account, amount: float):
        self.ammount = amount
        self.account = Account
        self.status = 'inactive'
        self.balance = 0.0
        self.id = 1
        self.date = datetime.date.today()