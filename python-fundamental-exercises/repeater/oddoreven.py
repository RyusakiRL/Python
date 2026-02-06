even = 0;
odd = 0;
limit = 1;

while limit<=6:
    number = int(input("Enter a number\n"))
    if number%2==0:
        even=even+1
    else:
        odd=odd+1
    limit=limit+1;

print(f"Had {even} even number, had {odd} odd numbers");