limit = 1;
sum = 0;

while limit<=7:
    number = int(input("Enter the numbers to sum\n"))
    sum = sum +number
    limit = limit+1;

print(f"The final sum is {sum}");