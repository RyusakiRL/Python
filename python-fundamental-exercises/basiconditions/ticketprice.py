distance = float(input("Write the distance traveled by the car\n"));

if distance<=200.0:
    print(f"The distance traveled is {distance} and the ticket price is R${distance*0.5}");
else:
    print(f"The distance traveled is {distance} and the ticket price is R${distance*0.45}");