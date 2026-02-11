def pa(init, endless, increment):
    sum = init
    
    while sum<=endless:
        print(sum, end = " ")
        sum+=increment

numb = int(input("Enter the first number\n"))
end = int(input("Enter the last number\n"))
increment = int(input("Enter the increment\n"))

pa(numb,end,increment)