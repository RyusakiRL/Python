totalm = 0;
totalf = 0;
continue2 = "yes"
while continue2!="no":
    
    gender = input("Write the gender (male or female)\n")
    salary = float(input("Enter the salary\n"))

    if gender == "male":
        totalm+=salary;
    elif gender == "female":
        totalf+=salary;

    continuesz = input("You want to continue?\n")

    continue2 = continuesz;

print("------RESULTS------\n");
print(f"Total salary payed to mans R${totalm}");
print(f"Total salary payed to womans R${totalf}");