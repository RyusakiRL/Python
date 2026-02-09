limit = 1;
vectorios = []

while limit<=7:
    name = input("Insert the name\n")

    vectorios.append(name)
    limit+=1;

invert = vectorios[::-1]

print(invert);
