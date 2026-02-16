list_stock = {}

def stock_management(liststock, action, item, quantity, price):

    if action == "add":
        if item in list_stock:
            list_stock[item]["Quantity"] += quantity
        else:
            list_stock[item] = {"Quantity": quantity, "Price": price}
        print(f"Sucess! {item} updated in stock.")

    elif action == "sell":
        
        if item in list_stock:                
            if list_stock[item]["Quantity"]>0:
                list_stock[item]["Quantity"]-=quantity
                print(f"Sale realized!! Value:{list_stock[item]['Price']*quantity:.2f}")
                print(f"Quantity in stock is:{list_stock[item]['Quantity']}")
            else:
                print("Insufficient quantity")
        else:
            print("Item not found")
while True:
    
    act = input("Type: 'add', 'sell', 'exit'\n")

    if act == "add":
        name = input("Type the name of item\n")
        quantities = int(input("Type the quantity you want to add\n"))
        prices = int(input("Type the price of product\n"))
        stock_management(list_stock, act, name, quantities, prices)
    
    elif act == "sell":
        name = input("Type the name of item\n")
        quantities = int(input("Type the quantity you want to sell\n"))
        stock_management(list_stock, act, name, quantities, 0)
    
    elif act == "exit":
        break
    else:
        print("Invalid command!!!")