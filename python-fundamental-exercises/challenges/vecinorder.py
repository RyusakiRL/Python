import random
vectorios = []


for i in range(20):
    number = random.randint(0,99)
    vectorios.append(number);

vectoriosordened = sorted(vectorios);

print("The original is:\n", vectorios)
print("The vector in order:\n", vectoriosordened)