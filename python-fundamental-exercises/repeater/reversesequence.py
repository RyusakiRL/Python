number = 30;

while number>=0:
    if number%4!=0:
        print(f"{number}", end=" ")
    elif number%4==0:
        print(f"[{number}]", end=" ")

    number = number-1;

print("End!");