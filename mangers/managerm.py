from manager import Manager

class Manager:
    managers = []
    
    def create_manager(self, email: str, password: str, first_name: str, last_name=None, middle_name=None):                     
        manager_id = self._id
        manager = Manager(id=owner_id, email=email, first_name=first_name, password=password)                    
        manager.last_name = last_name
        manager.middlename = middle_name
        manager.phone = phone
        return True
    
    def login(self, email: str, password: str):
        for manager in self.managers:
            if manager.email == email and manager.password == password:
                return manager
            else:
                return False
            
    def change_password(self, email: str, password: str):
        for manager in self.managers:
            if manager.password == password:
                return manager
            else:
                return False
            
    def delete_manager(self, email:str):
        manager = self.__find(email)
        if manager is None:
            return False
        else:
            self.managers.remove(manager)
            return True
        
    def search(self, email: str):
        manager = self.__find(email)
        if manager is None:
            return False
        else:
            self.__show(manager)
            
    def id(self):
        return self.id
            
            
    def show(self, manager: Manager):
        print(manager.id, ' ', ' ', manager.first_name, ' ', manager.middle_name,manager.last_name, ' ', manager.email, ' ', manager.phone)
             



   

