import random

limit = 1;
vectorios = []

while limit<=7:
    number = random.randint(1,99999999)

    vectorios.append(number)
    
    limit+=1;

print(vectorios)