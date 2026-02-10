ages = []

for i in range(8):
    age = int(input("Enter the people age: \n"))
    ages.append(age)

average = sum(ages)/len(ages)
print(f"\nThe average of age is: {average:.2f}")


print("\nPositions with people over 25 years:")
for i, age in enumerate(ages):
    if age>25:
        print(f"Position: {i} (Age: {age})");

biggest_age = max(ages)
print(f"The biggest age is: {biggest_age}")


print("Positions where appears the biggest age:")
for i, age in enumerate(ages):
    if age == biggest_age:
        print(f"Position: {i}")