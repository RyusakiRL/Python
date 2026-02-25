class BankAccount():
    def __init__(self, holder, balance = 0):
        self.holder = holder
        self.balance = balance
    
    def deposit(self, value):
        self.balance+=value
        print(f"[{self.holder}] Deposited R${value:.2f}. Actual balance: R${self.balance:.2f}")
    

class SavingAccount(BankAccount):
    def __init__(self, holder, balance=0, interest_rate=0.05):
        super().__init__(holder, balance)
        
        self.interest_rate = interest_rate
    
    def yield_interest(self):
        interest = self.balance*self.interest_rate
        print(f"[{self.holder}] Yielding interest of {self.interest_rate * 100}%...")

        self.deposit(interest)

print("--- TESTANDO A CONTA NORMAL ---")
conta_comum = BankAccount("Caio")
conta_comum.deposit(100)

print("\n--- TESTANDO A CONTA POUPANÇA ---")
conta_poupanca = SavingAccount("João", 100)

conta_poupanca.yield_interest()