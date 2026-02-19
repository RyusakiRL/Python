while True:
    print("\n=======SELL BOOK========")
    print("1 - Sell register")
    print("2 - See total of day")
    print("3 - Exit")

    option = input("Choose a option: ")
    

    if option == "1":
        value = float(input("Enter the value: "))

        with open("sell.txt", "a") as arquive:
            arquive.write(f"{value}\n")
        
        print("Sell Registered with sucess!")

    elif option == "2":
        total = 0

        try:
            with open("sell.txt", "r") as arquive:
                for line in arquive:
                    value = float(line.strip())
                    total += value
            
            print(f"The total sell today is {total:.2f}")
        
        except FileNotFoundError:
            print("No one sell registered now")
    
    elif option == "3":
        print("Closing the box")
        break

    else:
        print("Invalid option!")