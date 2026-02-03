name = input("Write the employee name\n");
salary = float(input("Write the salary value\n"));
years = int(input("How many years he worked in the emprise\n"));

if years<3:
    print(f"Hello {name}, your salary adjustment is {salary*1.03}");
elif years>=3 and years<=10:
    print(f"Hello {name}, your salary adjustment is {salary*1.125}");
elif years>10:
    print(f"Hello {name}, your salary adjustment is {salary*1.2}");