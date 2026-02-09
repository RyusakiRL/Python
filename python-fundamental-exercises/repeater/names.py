continuesz = "yes"
namesz = ""
oldpeople = 0;
youngw = 999999999999999999;
quantitypeople = 0;
over30 = 0;
below18 = 0;
namew = "";
sumage = 0;

while continuesz != "n":
    name = input("What is your name?\n")
    age = int(input("Enter the age\n"))
    gender = input("What is your gender? (f for female and m for male)\n")
    
    quantitypeople+=1;
    sumage += age;

    if age>oldpeople:
        namesz = name
        oldpeople = age;
    
    if gender == "f" and age<youngw:
        youngw = age
        namew = name;

    if gender == "m" and age>30:
        over30= over30 + 1;

    if gender == "f" and age<18:
        below18= below18 +1;

    continueshiny = input("You want to continue? (y for yes and n for no)\n")
    continuesz = continueshiny;

print("--------------------------RESULTS--------------------------")
print(f"The name of oldest person is {namesz}");
print(f"The name of youngest woman is {namew} ");
print(f"The age average of group is {sumage/quantitypeople}");
print(f"Quantity of mans over age 30 is {over30} ");
print(f"Quantity of womans below of age 18 is {below18}");
