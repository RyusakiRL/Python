car = input("What is the type of car (luxe or popular)\n");
day = int(input("How many days you keep with the car\n"));
distance = float(input("How many distance the car traveled?\n"));

if car == "popular" and distance<=100.0:
    value_total = (distance*0.2) + (90*day);
    print(f"The total value is ${value_total}");

elif car == "popular" and distance>100.0:   
    value_total = (distance*0.1) + (90*day);
    print(f"The total value is ${value_total}");



if car == "luxe" and distance<=200:
    value_total = (distance*0.3) + (150*day);
    print(f"The total value is ${value_total}");

elif car == "luxe" and distance>200.0:   
    value_total = (distance*0.25) + (150*day);
    print(f"The total value is ${value_total}");