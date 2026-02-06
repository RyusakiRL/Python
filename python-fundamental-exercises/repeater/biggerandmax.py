bigger = 0;
lower = float('inf');
limit = 1;

while limit<=8:
    number = int(input("Enter a number\n"));
    
    if number<lower:
        lower = number;
    
    if number>bigger:
        bigger = number;
    limit += 1;

print(f"The biggest number is {bigger} and the lowest is {lower}");

