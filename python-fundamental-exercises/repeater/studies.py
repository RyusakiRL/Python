quantitystudents = 0;
agesz = 0;
avgage = 0;

while agesz!=999:
    age = int(input("Enter the age of student\n"))

    if age!=999:
        quantitystudents+=1
        avgage+=age;

    agesz=age;

print(f"Have {quantitystudents} students and the average age is {avgage/quantitystudents}")
