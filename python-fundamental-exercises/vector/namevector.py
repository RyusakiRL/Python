namev = []
genderv = []
salaryv = []

for i in range(5):
    name = input("Enter the name\n")
    gender = input("Enter the gender (m for male f for female)\n")
    salary = int(input("Enter the salary\n"));
    namev.append(name)
    genderv.append(gender)
    salaryv.append(salary)

print("\n--- Resultados ---")

for i, gender in enumerate(genderv):

    if genderv[i] == "f" and salaryv>5000:
                    
        print(namev[i])
        print(salaryv[i])