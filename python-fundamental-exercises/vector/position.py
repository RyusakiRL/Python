vectorios = []
limit = 1
position = 0
positionv = []

while limit<=5:
    number = int(input("Enter a number\n"));
    vectorios.append(number)

    if number%10 == 0:
        positionv.append(position);

    position+=1
    limit+=1;


print("Had a divisible by 10 in positions ", positionv)
