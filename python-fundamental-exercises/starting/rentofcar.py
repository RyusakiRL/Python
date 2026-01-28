distance = float(input("is What the distance traveled with the car in km?\n"));
days = int(input("How many days you rented the car?\n"));

final_price = distance*0.20+days*90;

print(f"The final price to pay is R${final_price}");