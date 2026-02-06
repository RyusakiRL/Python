biggest = 0;
limit = 1;
average = 0;
over18 = 0;
belo5 = 0;

while limit<=10:
    age = int(input("Enter the age\n"));
    average+=age

    if age>18:
        over18+=1;

    elif age<5:
        belo5+=1;

    elif age>biggest:
        biggest = age;
    
    limit+=1;

print(f"Had {belo5} with age below of five years, had {over18} above of eighteen years, the biggest number is {biggest} and the average is {average/10}");