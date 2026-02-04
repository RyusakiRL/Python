a = float(input("Write the first size side of triangle\n"));
b = float(input("Write the second size side of triangle\n"));
c = float(input("Write the third size side of triangle\n"));

if a<b+c and b<c+a and c<b+a:
    x = "exists";
else:
    x = "don't exist";
    print("The triangle don't exist");


if x=="exists" and a==b and b==c:
    print("Is a equilateral triangle");
elif x=="exists" and a!=b and b!=c and a!=c:
    print("Is a scalene triangle");
elif x=="exists" and a==b and b!=c or x=="exists" and b==c and a!=c or x=="exists" and a==c and c!=b:
    print("Is a isosceles triangle");