import random

number = random.randint(1, 5);



while True:
    x = int(input("Enter a number of 1 to 5\n"))

    if x!=number:
        print("You lost, try again")

    if x == number:
        print("You won")
        break
