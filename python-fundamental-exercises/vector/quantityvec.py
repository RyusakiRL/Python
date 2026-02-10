import random
limit = 0;
limit2 = 0;
vectorios = []
positions = []
quantity = 0;


while limit<=29:
    number = random.randint(1,15)
    vectorios.append(number)
    limit+=1;

number2 = int(input("Enter the number\n"));

while limit2<=29:
    if number2==vectorios[limit2]:
        positions.append(limit2)
        quantity+=1;
    limit2+=1;

print("----------------RESULTS----------------");
print("Positions of the number choosed", positions);
print(f"Quantity encountered {quantity}");