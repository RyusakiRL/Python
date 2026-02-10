vectorname = []
vectorage = []

for i in range(9):
    name = input("Enter the name\n")
    age = int(input("Enter the age\n"))

    vectorname.append(name)
    vectorage.append(age);

print("People below 18:\n")

for i, age in enumerate(vectorage):

    if age<18:
        print(vectorname[i], end = " ")
        print(vectorage[i], "years")
        