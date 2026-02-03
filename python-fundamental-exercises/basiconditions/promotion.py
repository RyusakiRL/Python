name = input("Write your name\n");
gender = input("What is your gender male or female?\n");
value = int(input("Write down the value of purchases\n"));

gender2 = gender.islower;

if gender == "male": 
    print(f"Hello {name}, the value of purchase is {value*0.95}");
else:
    print(f"Hello {name}, the value of purchase is {value*0.87}");