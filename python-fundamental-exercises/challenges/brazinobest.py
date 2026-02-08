import random

number = random.randint(1, 10);
limit = 1;

while limit<=4:
    number2=int(input("Enter a number of 1 to 10\n"))

    if number==number2:
        print("You won")
        break
    elif number!=number2 and limit<=3:
        print("Try again");

    limit+=1;

if limit == 5:
    print("You lose");