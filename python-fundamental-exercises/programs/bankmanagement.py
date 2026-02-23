class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self.balance = balance

    def deposit(self, value):
        self.balance+=value

    def withdraw(self, value):
        if self.balance>=value:
            self.balance-= value
            print(f"Actual balance is R${self.balance:.2f}")
            return True
        else:
            print("Insufficient balance")
            return False
        
    def transfer(self, value, destination_account):
        if self.balance>=value:
            self.balance-=value
            destination_account.deposit(value)

            print("Transferred with sucess!!")
            return True
        else:
            print("Insufficient balance for transfer")
    
    def see_balance(self):
        print(f"Actual balance is R${self.balance:.2f}")

account_list = []

while True:
    print("==========================================MENU==========================================")
    action = input("Type: 'new account', 'deposit', 'withdraw', 'transfer' or 'exit': ")

    if action == "new account":
        name = input("Type the name: ")
        new_account = BankAccount(name)
        account_list.append(new_account)
        print(f"Account for {name} created successfully!")

    elif action == "deposit":
        name_deposit = input("Type the name: ")
        
        try:
            value = float(input("Insert the quantity R$"))
            account_deposit = None
            
            for account in account_list:
                if account.holder == name_deposit:
                    account_deposit = account
                    print(f"{name_deposit}:")
                    account_deposit.deposit(value)

                    account_deposit.see_balance()
                    break
                else:
                    print("Not encountered account")

        except ValueError:
            print("invalid value!!")
    
    elif action == "withdraw":
        name_withdraw = input("Type the name: ")
        
        try:
            value = float(input("Insert the quantity R$"))
            account_withdraw = None

            for account in account_list:
                if account.holder == name_withdraw:
                    account_withdraw = account
                    print(f"{name_withdraw}:")
                    account_withdraw.withdraw(value)
                    break
                else:
                    print("Not encountered account")

        except ValueError:
            print("invalid value!!")
    
    elif action == "transfer":
        name_origin = input("Type your name: ")
        name_destin = input("Type the destination name: ")
        
        account_origin = None
        account_destin = None
        try:
            value = float(input("Insert the quantity R$"))
            
            for account in account_list:
                
                if account.holder == name_origin:
                    account_origin = account

                elif account.holder == name_destin:
                    account_destin = account
                break
            if account_destin!= None and account_origin!= None:
                account_origin.transfer(value, account_destin)
                print(f"{name_origin}:")
                account_origin.see_balance()
            
            else:
                print("One or both accounts not encountered")
        except ValueError:
            print("invalid value!!")
    
    elif action == "exit":
        break

    else:
        print("Invalid command")