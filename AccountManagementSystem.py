from managers.AccountHolderManager import AccountHolderManager
from managers.Manager import ManagerManager
from managers.AccountManager import AccountManager
from managers.loanloan import LoanManger
from managers.overdraftmanager import OverdraftManager


account_holder_manager = AccountHolderManager()
manager = ManagerManager()
account_manager = AccountManager()
loan_manager = LoanManger()
overdraft_manager = OverdraftManager() 


def main_menu():
    print(
        "Welcome to  MYBank" '\n' "Enter 0 to Quit" '\n' "Enter 1 to go to Account Holder Menu" '\n' 'Enter 2 to go to Manager Menu' '\n' "Enter 3 to go "
        "to Account Menu" '\n' 'Enter 4 to go to Loan Menu' '\n' 'Enter 5 to go to Overdraft Menu')


def show_sub_menu(option):
    if option == 0:
        print('Thank you for using  MYBank')
    elif option == 1:
        show_account_holder_menu()
        action = int(input())
        if action == 0:
            main_menu()
            
        else:
            handle_account_holder_menu(action)
    elif option == 2:
        show_manager_menu()
        action = int(input('Please choose an option from the above options: '))
        if action == 0:
            mainMenu()
        else:
            handle_manager_menu(action)
    elif option == 3:
        show_account_menu()
        action = int(input())
        if action == 0:
            main_menu()
        else:
            handle_account_menu(action)
    elif option == 4:
        show_loan_menu()
        action = int(input())
        if action == 0:
            main_menu()
        else:
            handle_loan_menu(action)
    elif option == 5:
        show_overdraft_menu()
        action = int(input())
        if action == 0:
            main_menu()
        else:
            handle_overdraft_menu(action)


def show_account_holder_menu():
    print(
        "Enter 1 to Register"'\n'"Enter 2 to update your details"'\n'"Enter 3 to change password"'\n'"Enter 4 to search"
        '\n'
        "Enter 5 to delete an account holder"'\n'"Enter 6 to list"'\n'"Enter 0 to go back")


def show_manager_menu():
    print("Enter 1 to create a manager account" '\n' "Enter 2 to log into your manager account" '\n' "Enter 3 to edit your manager account" '\n' "Enter 4 to view your manager account details" '\n'
          '\n' "Enter 5 to go back")


def show_account_menu():
    print(
        "Enter 1 to deposit"'\n'"Enter 2 to withdraw"'\n'"Enter 3 to block account"'\n'"Enter 4 to unblock an account")

def show_loan_menu():
    print( "Enter 1 to obtain loan" '\n' 'Enter to to pay back a pending loan' '\n''Enter 2 to list loan details' '\n' 'Enter 3 to view loan details' )

def show_overdraft_menu():
    print("Enter 1 to obtain an overdraft" '\n' "Enter 2 to payback a pending overdraft" '\n' "Enter 3 to list overdraft details" '\n' "Enter 4 to view overdraft details")
      
 
   


def handle_account_holder_menu(action):
    if action == 1:
        email = str(input('Enter Your E-Mail Address: '))
        password = str(input('Enter Your Password: '))
        confirm_password = str(input('Confirm Your Password: '))
        first_name = str(input(
            'Enter Your First Name: '))
        last_name = str(input(
            'Enter Your Last Name' '\t' 'if the last name is not given None will be used: '))
        middle_name = str(input(
            'Enter Your Middle Name' '\t' 'if the middle name is not given None will be used: '))
        phone = str(input(
            'Enter Your Phone Number' '\t' 'if phone number is not given None will be used: '))
        pin = int(input('Please Enter a 4 digit pin: '))
        holder = account_holder_manager.create_account_holder(
            email=email, password=password, confirm_password=confirm_password, first_name=first_name,
            last_name=last_name, phone=phone, middle_name=middle_name)
        if holder is False:
            print('Password is incorrect')
        else:
            account_number = account_manager.create_account(
                account_holder=holder, pin=pin)
            print('Account Created Succesfully, Your Account Number Is: ', account_number)

    elif action == 2:
        email = str(input('Enter Your E-Mail Address: '))
        password = str(input('Enter Your Password: '))
        holder = account_holder_manager.login(email=email, password=password)
        if holder is False:
            print('E-Mail Or Password Incorrect')
        else:
            first_name = str(input(
                'Enter Your First Name'))
            last_name = str(input(
                'Enter Your Last Name' '\t' 'if the last name is not given None will be used: '))
            middle_name = str(input(
                'Enter Your Middle Name' '\t' 'if the middle name is not given None will be used: '))
            phone = str(input(
                'Enter Your Phone Number' '\t' 'if phone number is not given None will be used: '))
            new_holder = account_holder_manager.update_account_holder(
                email=email, first_name=first_name, last_name=last_name, phone=phone, middle_name=middle_name)
            if new_holder is True:
                print('Update Valid')
            else:
                print('Update Invalid')

    elif action == 3:
        email = str(input('Enter Your E-Mail Address: '))
        new_password = str(input('Enter The New Password: '))
        status = account_holder_manager.change_password(
            email=email, new_password=new_password)
        if status is True:
            print('Password Successfully Changed')
        else:
            print('Information Invalid')

    elif action == 4:
        email = str(input('Enter Your E-Mail Address: '))
        holder = account_holder_manager.search(email=email)
        if holder is False:
            print('Not Found')

    elif action == 5:
        email = str(input('Enter Your E-Mail Address: '))
        password = str(input('Enter Your Password: '))
        holder = account_holder_manager.login(email=email, password=password)
        if holder is False:
            print('Password Incorrect')
        else:
            status = account_holder_manager.delete_account_holder(email=email)
            if status is True:
                print('Account Deleted')
            else:
                print('Account not deleted')

    elif action == 6:
        account_holder_manager.list_account_holders()

    show_sub_menu(1)


def handle_manager_menu(action):
    if action == 1:
        email = str(input('What Is Your E-Mail: '))
        password = str(input('Enter Your Password: '))
        confirm_password = str(input('Confirm Your Password: '))
        first_name = str(input('Enter Your First Name: '))
        middle_name = str(input('Enter Your Last Name: '))
        last_name = str(input('Enter Your Last Name: '))
    
        manager = manager.create_manager(email=email, password=password, confirm_password=confirm_password,first_name=first_name, last_name=last_name)
        if manager is True:
            print('Manager Account Creation Sucessful')
        else:
            print('Wrong Account Details Try Again')

    elif action == 2:
        email = str(input('Enter Your E-Mail Address: '))
        password = str(input('Enter Your Password: '))
        manager = manager.login(
            email=email, password=password,)
        if manager is False:
            print('Your Password Is Incorrect')
        else:
            first_name = str(input('Enter Your First Name: '))
            last_name = str(input('Enter Your Last Name: '))
            middle_name = str(input('Enter Your Last Name: '))
            phone = str(input('Enter your phone Number: '))
            new_holder = manager.update_manager(
                email=email, first_name=first_name, last_name=last_name, middle_name=middle_name, phone=phone, password=password)
        if new_holder is True:
            print('Update Sucessful')
        else:
            print('Update Not Sucessful')

    elif action == 3:
        password = str(input('Enter Your Password: '))
        new_password = str(input('Enter Your New Password: '))
        status = manager.change_password(
            password=password, new_password=new_password)
        if status is True:
            print('Password Successfully Changed')
        else:
            print('INVALID INFORMATION')

    elif action == 4:
        manager.view_details()

    elif action == 5:
        mainMenu()
    show_sub_menu(2)


def handle_account_menu(action):
    if action == 1:
        account_number = str(input('Enter Your Account Number: '))
        pin = int(input('Enter Your Pin: '))
        amount = float(input('Enter The Amount You Want To Deposit: '))
        status = account_manager.deposit(
            pin=pin, amount=amount, account_number=account_number)
        if status is False:
            print('Operation Unsuccessful Check Your Details ' )
        else:
            print('Operation Successful')

    elif action == 2:
        account_number = str(input('Enter Your Account Number: '))
        pin = int(input('Enter Your Account Pin: '))
        amount = float(input('Enter The Amount You Wish To Withdraw: '))
        status = account_manager.withdraw(
            pin=pin, amount=amount, account_number=account_number)
        print(status.get('message'))

    elif action == 3:
        account_number = str(input('Enter Your Account Number: '))
        account_manager.block_account(account_number=account_number)

    elif action == 4:
        account_number = str(input('Enter Your Account Number: '))
        account_manager.unblock_account(account_number=account_number)
    show_sub_menu(3)
    
def handle_loan_menu(action):
    if action == 1:
        account_number = str(input('Enter Your account Number: '))
        pin = int(input('Enter Your pin: '))
        print(
            'Enter 0 for Household Loan Amount: 'f'{loan_manager.loan_types.get("household")}"\n' 'Enter 1 for Car Loan: '
            f'{loan_manager.loan_types.get("car")}"\n' 'Enter 2 for School fees Loan: 'f'{loan_manager.loan_types.get("school fee")}" \n' 'Enter 3 For Business Loan: '
            f'{loan_manager.loan_types.get("business")}"\n' 'Enter 4 for Emergency loan: 'f'{loan_manager.loan_types.get("emergency")}"')
        val = int(input())
        loan_type = handle_loan_type(val)
        number_of_mounts = int(input('Enter numbers of months to pay back'))
        account = account_manager.return_account(account_number=account_number, pin=pin)
        loan = loan_manager.create_loan(account=account, loan_type=loan_type, number_of_months=number_of_mounts)
        try:
            if loan['not_granted']:
                print(loan['not_granted'])
        except KeyError:
            print(loan['message'])
            
    elif action == 2:
        loan_manager.list_loans()
    
    elif action == 3:
        loan_manager.view_details()


def handle_loan_type(val: int):
    loan_names = ['household', 'car', 'school fee', 'business', 'emergency']
    for name in range(len(loan_names)):
        if val == name:
            return loan_names[name]
        
    show_sub_menu(4)
        
def handle_overdraft_menu(action):
    if action == 1:
        account_number = str(input('Enter your account number: '))
        pin = int(input("Enter four your digit pin: "))
        amount = float(input('Enter the amount you wish to obtain: '))
        account = account_manager.return_account(account_number=account_number, pin=pin)
        if account is False:
            print("Account not found ")
        else:
            overdraft = overdraft_manager.create_overdraft(account=account, amount=amount)
            print('Overdraft Successfully Obtained')
        
    elif action == 2:
        account_number = str(input('Enter Your Account Number: '))
        pin = int(input('Enter your 4 digit pin: '))
        amount = float(input('Enter the amount you wish to payback: '))
        account = account_manager.return_account(account_number=account_number, pin=pin)
        overdraft = overdraft_manager.pay_back_overdraft(account_number=account_number)
        
    # elif action == 3:
    #     overdraft_manager.list_overdrafts()
        
    # elif action == 4:
    #     overdraft_manager.view_details()
    
   

def main():
    flag = True
    while flag:
        main_menu()
        option = int(input())
        if option == 0:
            flag = False
        else:
            show_sub_menu(option)


main()
