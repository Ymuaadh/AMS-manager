from models.overdraft import Overdraft
from models.Account import Account
from typing import List
import datetime


class OverdraftManager:
    overdrafts: List[Overdraft] = []
    

    def create_overdraft(self, account: Account, amount: float):
        active_account = self.__is_account_active(account)
        if active_account is True:
            if amount <= 100000.00:
                overdraft_status = self.__is_overdraft_not_active(account_number=account.account_number)
                if overdraft_status is False:
                    overdraft = Overdraft(amount=amount, account=account)
                    overdraft.id = self.__get_id()
                    overdraft.balance = account
                    account.balance -= amount
                    overdraft.date = datetime.date.today()
                    reply = 'Overdraft Succesful'
                    return reply
                else:
                    reply = 'You have already collected an overdraft, Please pay up'
                    return reply
            else:
                reply = 'You cannot collect more than 100 000'
                return reply
        else:
            reply = 'Account is inactive'
            return reply
            
            
    def pay_back_overdraft(self, account_number: str, amount: float):
        overdraft = self.__get_overdraft(account_number=account_number)
        if overdraft is not False:
            overdraft.balance -= amount
            for overdraft in overdrafts:
                if overdraft.balance == 0:
                    overdraft.status == 'inactive'
                    reply = 'Overdraft has been  paid'
                    return reply
                else:
                    reply = 'Removed from overdraft'
                    return reply
        else:
            reply = 'No active overdraft found'
            return reply             
                    
    def __check__amount__overdraft(self, account_number: str):
        for Overdraft in self.overdrafts:
            if Overdraft.amount <= 100000:
                return True
        return False

    
    def __get_overdraft_initial_balance(self,  amount: float):
            val = 100000 
            amount = val
            return amount       
        


    def __check_if_no_active_overdraft(self, account_number: str):
            for overdraft in self.overdrafts:
                if overdraft.account.account_number == account_number:
                    if overdraft.status == 'active':
                        return True
            return False
    
    def view_details(self):
        print(self.overdraft.id, '.', ' ', self.overdraft.balance, ' ' 
                '\t', self.overdraft.date )
        
    def list_overdrafts(self):
        for overdraft in self.overdrafts:
            self.__show(overdraft)
    

    def __get_id(self):
        length = len(self.overdrafts)
        if length == 0:
            length += 1
            return length
        else:
            for overdraft in self.overdrafts:
                if overdraft.id == length:
                    length += 1
                    return length
                else:
                    continue
                
    def __get_overdraft(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                if overdraft.status == 'active':
                    return overdraft
                else:
                    return False

    def __is_account_active(self, account: Account):
        if account.account_status == 'inactive':
            return False
        else:
            return True

    def __is_overdraft_not_active(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.status == 'active':
                if overdraft.account.account_number == account_number:
                    return True
        return False

    def __show(self, overdraft: Overdraft):
        print(
              overdraft.id, '.', ' ', overdraft.account.account_number, ' ',overdraft.account.account_holder.first_name," ", overdraft.amount,
              ' ', '\t', overdraft.balance, )
