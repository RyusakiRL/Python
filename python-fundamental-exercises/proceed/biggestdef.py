def bigger(numberone, numbertwo):
    if numberone>numbertwo:
        print("The first number is the biggest")
    elif numberone==numbertwo:
        print("The first number is equal to second")
    else:
        print("The second number is the biggest");

number1 = int(input("Enter the first number\n"))
number2 = int(input("Enter the second number\n"));

bigger(number1, number2)