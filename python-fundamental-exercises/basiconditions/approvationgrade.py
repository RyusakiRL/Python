gradeone = float(input("Enter the first grade\n"));
gradetwo = float(input("Enter the second grade\n"));

average = (gradeone+gradetwo)/2.0;

if average<=4.9:
    print(f"Your average is {average}, reproved");
elif average>=5.0 and average<=6.9:
    print(f"Your average is {average}, recuperation");
elif average>=7.0:
    print(f"Your average is {average}, approved");