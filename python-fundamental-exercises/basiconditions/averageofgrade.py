name = input("is What your name?\n");
grade1 = float(input("Is What your first note?\n"));
grade2 = float(input("Is what your second note?\n"));
average = (grade1+grade2)/2.0;
if average>=7.0:
    print(f"Hello {name}, your average is {average}, approved");
else:
    print(f"Hello {name}, your average is {average}, reproved");