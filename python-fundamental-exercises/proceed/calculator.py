def calculator(number1, operator, number2):
    match operator:
        case "+":
            print(number1+number2)
        case "-":
            print(number1-number2)
        case "x":
            print(number1*number2)
        case "*":
            print(number1*number2)
        case "/":
            if number2 == 0:
                print("Impossible to divide by 0")
            else:
                print(number1/number2);

numberone = int(input("Insert the first number\n"))
operator = input("Insert the operator\n")
numbertwo = int(input("Insert the second number\n"))


print("-------RESULT-------")
calculator(numberone, operator, numbertwo)