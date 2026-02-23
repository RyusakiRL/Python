class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self.balance = balance

    def deposit(self, value):
        self.balance+=value

    def sake(self, value):
        if self.balance>=value:
            self.balance-= value
            return True
        else:
            print("Insufficient balance")
            return False
        
    def transfer(self, value, account):
        if self.balance>=value:
            self.balance-=value
            BankAccount(account).deposit+=value
            return True
        else:
            print("Invalid transfer")

while True:
    action = input("Type: 'new account', 'deposit', 'sake', 'transfer' or 'exit': ")

    if action == "new account":
        name = input("Type the name: ")
        new_account = BankAccount(name)
    
    elif action == "deposit":
        name = input("Type the name: ")
        new_account = name
        try:
            value = float(input("Insert the quantity R$"))
            new_account.deposit(value)

        except ValueError:
            print("invalid value!!")
    
    elif action == "sake":
        name = input("Type the name: ")
        new_account = name
        try:
            value = float(input("Insert the quantity R$"))
            new_account.sake(value)

        except ValueError:
            print("invalid value!!")
    
    elif action == "transfer":
        name = input("Type your name: ")
        name2 = input("Type the name of you want to transfer: ")
        new_account = name
        try:
            value = float(input("Insert the quantity R$"))
            new_account.deposit(value, name2)

        except ValueError:
            print("invalid value!!")
    
    elif action == "exit":
        break

    else:
        print("Invalid command")