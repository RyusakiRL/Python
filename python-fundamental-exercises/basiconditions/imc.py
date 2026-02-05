height = float(input("Enter your height\n"));
weight = float(input("Enter your weight\n"));

imc = weight/(height*height);

match imc:
    case _ if imc < 18.5:
        print("Underweight");
    case _ if imc>=18.5 and imc<25:
        print("Ideal weight");
    case _ if imc>=25 and imc<30:
        print("Overweight");
    case _ if imc>=30 and imc<40:
        print("Obesity");
    case _ if imc>=40:
        print("Morbid obesity");

print(f"Your imc is {imc:.2f}.");