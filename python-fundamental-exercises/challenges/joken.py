import random

number = random.randint(1, 3);

match number:
    case 1:
       number = "paper"
    case 2:
        number = "rock"
    case 3:
        number = "scissor"

joken = input("Choose between rock, paper or scissor\n");
jokenpo = joken.lower;

if number==joken:
    print(f"The machine choose {number} and you {joken}, Draw");

elif number=="paper" and joken == "scissor":
    print(f"The machine choose {number} and you {joken}, you win");

elif number=="rock" and joken == "paper":
    print(f"The machine choose {number} and you {joken}, you win");

elif number=="scissor" and joken == "rock":
    print(f"The machine choose {number} and you {joken}, you win");

elif number=="scissor" and joken == "paper":
    print(f"The machine choose {number} and you {joken}, you lose");

elif number=="paper" and joken == "rock":
    print(f"The machine choose {number} and you {joken}, you lose");

elif number=="rock" and joken == "scissor":
    print(f"The machine choose {number} and you {joken}, you lose");