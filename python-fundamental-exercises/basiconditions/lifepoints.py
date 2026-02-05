exercise = int(input("How much time in hours, you do in exercise this month\n"));

match exercise:
    case _ if exercise<=10:
        print(f"You trained {exercise} hours, gaining ${exercise*2*0.05}");
    case _ if exercise>10 and exercise<=20:
        print(f"You trained {exercise} hours, gaining ${exercise*5*0.05}");
    case _ if exercise>20:
        print(f"You trained {exercise} hours, gaining ${exercise*10*0.05}");