continuingsz = "Yes";    
biggerage = 0;
minorage = 999999;
manquantity = 1;
sumanage = 0;

while continuingsz!="no":
    gender = input("What is your gender? (male or female)\n")
    age = int(input("What is your age?\n"))

    if age>biggerage:
        biggerage = age
        sumanage+=age

    elif gender == "male":
        manquantity+=1;

    elif gender == "female" and age<minorage:
        minorage=age

    continuing = input("You want continue (yes or no)?\n")
    continuingsz = continuing;

print("----RESULTS----")
print(f"The big age is {biggerage}");
print(f"Quantity of mans {manquantity+1}");
print(f"The most young woman is {minorage}");
print(f"Average age of mans {sumanage/manquantity}");