class AccountHolder:

    def __init__(self, id: int, email: str, first_name: str):
        self.first_name = first_name
        self.middle_name = None
        self.last_name = None
        self.email = email
        self.__password = first_name
        self.phone = None
        self.id = id
        
    def change_password(self, password):
        self.__password = password
        return True
