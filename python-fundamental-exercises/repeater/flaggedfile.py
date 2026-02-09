sum = 0;
number = 0;
while number!=1111:
    number2 = int(input("Enter the number to sum (1111 to break)\n"))
    
    if number2!=1111:
        sum+=number2;
    
    number = number2

print(f"The sum total is {sum}")