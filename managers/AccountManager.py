import random

from models.Account import Account
from typing import List
from models.AccountHolder import AccountHolder


class AccountManager:

    accounts: List[Account] = []

    message = {}

    def create_account(self, account_holder: AccountHolder, pin: int):
        id = self.__get_id()
        accounts = Account(id=id, account_holder=account_holder, pin=pin)
        account_number = self.__get_account_number()
        accounts.account_number = account_number
        self.accounts.append(accounts)
        return account_number

    def deposit(self, pin: int, amount: float, account_number: str):
        account = self.__get_account(account_number=account_number)
        if account is not None:
            if account.pin == pin:
                account.balance += amount
                return True
            else:
                return False
        else:
            return False

    def withdraw(self, pin: int, amount: float, account_number: str):
        account = self.__get_account(account_number=account_number)
        if account is not None:
            if account.pin == pin and amount <= account.balance:
                if account.account_status == 'active':
                    account.balance -= amount
                    self.message['message'] = 'Withdrawal made!'
                    return self.message
                else:
                    self.message['message'] = 'not active, contact manager'
                    return self.message
            else:
                if account.balance < amount:
                    self.message['message'] = 'Insufficient funds'
                    return self.message
                else:
                    self.message['message'] = 'Incorrect Pin'
                    return self.message
        else:
            self.message['message'] = 'Account not found'
            return self.message

    def block_account(self, account_number):
        account = self.__get_account(account_number=account_number)
        account.account_status = 'inactive'
        return True

    def unblock_account(self, account_number):
        account = self.__get_account(account_number=account_number)
        account.account_status = 'active'
        return True
    
    def return_account(self, account_number: str, pin: int):
        account = self.__get_account(account_number=account_number)
        if account:
            if account.pin == pin:
                return account
            else:
                return False
        else:
            return False

    def __get_id(self):
        length = len(self.accounts)
        if length == 0:
            length += 1
            return length
        else:
            for account_holder in self.accounts:
                if account_holder.id == length:
                    length += 1
                    return length
                else:
                    continue

    def __get_account(self, account_number: str):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
            else:
                return False

    @staticmethod
    def __get_account_number():
        value = "MY"
        digit = str(random.randint(1000000, 9999999))
        account_number = value.upper() + digit
        return account_number
