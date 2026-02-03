a = float(input("Write the first side of triangle\n"));
b = float(input("Write the second side of triangle\n"));
c = float(input("Write the third side of triangle\n"));

if a<b+c and b<a+c and c<a+b:
    print("The triangle exists");
else:
    print("The triangle don't exist");