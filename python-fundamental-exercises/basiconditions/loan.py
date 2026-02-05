house = float(input("Enter the house value\n"));
salary = float(input("What is your salary?\n"));
years = int(input("How many years you pretend to pay?\n"));

monthyear = years*12;
prestation = house/monthyear;

if prestation<=salary*0.3:
    print("Loan approved");
else:
    print("Loan denied");