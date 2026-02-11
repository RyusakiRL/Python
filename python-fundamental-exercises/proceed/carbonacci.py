def fibonnaci(limit):

    after = 1
    before = 1
    sum = 1;
    for _ in range(limit-1):
        print(f"{sum}", end = ">>>>");
    
        sum = after+before
        before = after
        after = sum

        

limitless = int(input("Insert how much you want to see the fibonacci code\n"));
print("1", end=">>>>")
fibonnaci(limitless)
print("END!!")
    