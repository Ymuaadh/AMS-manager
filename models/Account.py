import datetime
from models.AccountHolder import AccountHolder


class Account:
    def __init__(self, id: int, account_holder: AccountHolder, pin: int):
        self.account_holder = account_holder
        self.balance = 0.0
        self.account_number = None
        self.date_created = datetime.date.today()
        self.account_status = 'active'
        self.pin = pin
        self.id = id
