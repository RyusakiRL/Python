limit = 1;
avg = 0;
countm = 0;
countf = 0;
avgm = 0;
over20 = 0;


while limit<=5:
    gender = input("What is your gender (male or female)?\n")
    age = int(input("What is your age?\n"))
    
    avg+=age

    if gender == "male":
        countm+=1
        avgm+=age;
    
    elif gender == "female":
        countf+=1;
    elif gender == "female" and age>20:
        over20+=1;

    limit+=1;
print("----------RESULTS----------");
print(f"Registered mans {countm}\n");
print(f"Registered womans {countf}\n");
print(f"Group average {avg/5}\n");
print(f"Man average {avgm/countm}");
print(f"Woman twenty over {over20}");
