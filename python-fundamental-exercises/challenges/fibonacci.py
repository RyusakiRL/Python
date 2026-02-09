after = 1
before = 1
sum = 1;
for i in range(10):
    print(f"{sum}");
    
    sum = after+before
    before = after
    after = sum
    