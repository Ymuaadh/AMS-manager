from models.Manager import Manager


class ManagerManager:

    manager: Manager

    def create_manager(self, email: str, password: str, confirm_password: str, first_name: str, last_name=None, phone=None):
        self.manager = Manager(email=email, first_name=first_name, password=password)
        self.manager.email = email
        self.manager.password = password
        self.manager.confirm_password = confirm_password
        self.manager.first_name = first_name
        self.manager.last_name = last_name
        self.id = 1
        self.manager.phone = phone
        return True

    def login(self, email: str, password: str):
        if email == Manager.email and password == Manager.password:
            return Manager
        else:
            return False
        
    def change_password(self, password: str, new_password: str):
        if password != new_password:
            return True
        else:
            return False

    def view_details(self):
        print(self.manager.id, '.', ' ', self.manager.first_name, ' ', self.manager.last_name,
              '\t', self.manager.email, ' ', self.manager.phone)
    


    def update_manager(self, email: str, first_name: None, last_name: None, phone: None):
        if self.manager is not None:
            self.manager.email = email
            self.manager.first_name = first_name
            self.manager.last_name = last_name
            self.manager.phone = phone
            return True
        else:
            return False
