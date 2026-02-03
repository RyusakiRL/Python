length = float(input("Write the length of terrain\n"));
large = float(input("Write the large of terrain\n"));

area = length*large;

if area<100.0:
    print(f"This is a Popular terrain, area {area}m²");
elif area>=100.0 and area<=500.0:
    print(f"This is a Master terrain, area {area}m²");
elif area>500.0:
    print(f"This is a VIP terrain, area {area}m²");