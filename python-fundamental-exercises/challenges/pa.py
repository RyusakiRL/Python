first = int(input("Enter the first number of P.A\n"));
increment = int(input("Insert the increment\n"));


for i in range(11):
    if i>=1:
        formule = first +(i-1)*increment;
        print(f"{formule}", end= " ")
