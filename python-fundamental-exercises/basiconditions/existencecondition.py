a = float(input("Write the first side of triangle"));
b = float(input("Write the second side of triangle"));
c = float(input("Write the third side of triangle"));

if a<b+c & b<a+c & c<a+b:
    print("The triangle exists");
else:
    print("The triangle don't exist");