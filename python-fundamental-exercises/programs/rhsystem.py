class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def got_payment(self):
        print(f"[{self.name}], salary received R${self.salary:.2f}")


class Dev(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)

        self.language = language
    
    def programmer(self):
        print(f"The dev [{self.name}] is writing the code in {self.language}")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def payment(self):
        total_salary = self.bonus+self.salary
        print(f"The payment of manager [{self.name}] is R${total_salary}") 

def search_for_payment(name, list):
    
        for name_search in list:
            name_of_employee = None

            if name_search.name == name:
                name_of_employee = name_search
                break

        if name_of_employee != None:
                    name_of_employee.got_payment()
        else:
            print("Name don't encountered")
            
manger = []
developer = []
employ = []

while True:
    print("========================MAIN MENU========================")
    action = str(input("Type: 'common employee', 'dev', 'manager' or 'exit': "))

    if action == "common employee":
        act = str(input("You want 'add' or 'give the salary'\n"))
        name_employee = str(input("Insert the name:"))

        if act == "add":
            try:
                salary_employee = float(input("Insert the salary R$"))
                new_com_employee = Employee(name_employee, salary_employee)
                employ.append(new_com_employee)
            except ValueError:
                 print("Enter a real value")
        
        elif act == "give the salary":
            search_for_payment(name_employee, employ)
    
    elif action == "dev":
            act = str(input("You want 'add', 'give the salary' or 'see status'\n"))
            name_dev = str(input("Insert the name:"))

            if act == "add":
                try:
                    salary_dev = float(input("Insert the salary R$"))
                except ValueError:
                     print("Insert a real number")
                     
                language = str(input("Insert the principal language: "))
                new_com_employee = Dev(name_dev, salary_dev, language)
                developer.append(new_com_employee)
            
            elif act == "give the salary":
                search_for_payment(name_dev, developer)
            
            elif act == "see status":
                for name_search in developer:
                    name_of_employee = None

                    if name_search.name == name_dev:
                        name_of_employee = name_search
                        break

                if name_of_employee != None:
                    name_of_employee.programmer()
                else:
                    print("Name don't encountered") 
    
    elif action == "manager":
        act = str(input("You want 'add' or 'give the salary'\n"))
        name_manager = str(input("Insert the name:"))

        if act == "add":
            try:
                salary_manager = float(input("Insert the salary R$"))
                bonus = float(input("Insert the bonus R$"))
                new_manager = Manager(name_manager, salary_manager, bonus)
                manger.append(new_manager)
            except ValueError:
                 print("Enter a real value")
        
        elif act == "give the salary":

            managers = None
            for name_search in manger:
                 
                 if name_search.name == name_manager:
                    managers = name_search
                    break
            if managers!= None:
                 managers.payment()
            else:
                 print("Name not encountered")     
    elif action == "exit":
        break