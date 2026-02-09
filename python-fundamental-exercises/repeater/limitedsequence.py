initnumber = int(input("Write the first number\n"));
lastnumber = int(input("Write the last number\n"));
increment = int(input("Write the increment\n"));

while initnumber<=lastnumber:
    print(f"{initnumber}", end=" ")
    initnumber = initnumber+increment;

print("End!");

