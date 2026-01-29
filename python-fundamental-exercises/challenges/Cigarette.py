cigarete = int(input("How many cigarettes you smoke per day?\n"));
years = int(input("How many years you smoked?\n"));

totalyearslost = (cigarete*years)/144;

print(f"You lost {totalyearslost} days of life");