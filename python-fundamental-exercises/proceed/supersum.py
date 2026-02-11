def supersum(first, second):
    
    frnumber = first
    lastn = second
    supersum = 0

    while frnumber<=lastn:
        print(frnumber, end="+")
        supersum+=frnumber
        frnumber+=1
        
    print("=", supersum)

number1 = int(input("Insert the first number\n"))
number2 = int(input("Insert the second number\n"))


supersum(number1,number2)