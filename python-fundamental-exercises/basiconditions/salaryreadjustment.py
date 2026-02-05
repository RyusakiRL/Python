salary = float(input("Write the actual salary of employee\n"));
gender = input("Input the gender of employee (male or female)\n");
time = float(input("Input how much time the employee worked in the enterprise in years\n"));


match gender:
    case _ if gender == "female" and time<15:
        print(f"The salary readjustment is ${(salary*1.05):.2f}")
    case _ if gender == "female" and time>=15 and time<=20:
        print(f"The salary readjustment is {(salary*1.12):.2f}")
    case _ if gender == "female" and time>20:
        print(f"The salary readjustment is {(salary*1.23):.2f}")
 
    case _ if gender == "male" and time<20:
        print(f"The salary readjustment is ${(salary*1.03):.2f}")
    case _ if gender == "male" and time>=20 and time<=30:
        print(f"The salary readjustment is {(salary*1.13):.2f}")
    case _ if gender == "male" and time>30:
        print(f"The salary readjustment is {(salary*1.25):.2f}");