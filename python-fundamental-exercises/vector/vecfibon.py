after = 1
before = 1
sum = 1;
vectorios = []
for i in range(15):
    vectorios.append(sum)
    sum = after+before
    before = after
    after = sum;


print(vectorios)
    