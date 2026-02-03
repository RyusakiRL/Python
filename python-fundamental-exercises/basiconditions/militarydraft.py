year = int(input("What is your year of birth?\n"));

age = 2026-year;

if age<18:
    print(f"There are {18-age} year left to military enlistment \n");
else:
    print(f"There are {age-18} years passed of military enlistment")