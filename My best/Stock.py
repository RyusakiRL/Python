import json

ARCHIVE = "shop_stock.json"

def save(list_to_save):
    with open(ARCHIVE, "w") as file:
           json.dump(list_to_save, file, indent=4);

def load_date():
    try:
        with open (ARCHIVE, "r") as file:
            return json.load(file)
    except FileNotFoundError:

        return [
    {"Mark": "Tagima", "price": 832.00, "quantity": 15},
    {"Mark": "Konig", "price": 500.00, "quantity": 12},
    {"Mark": "Yamaha", "price": 1320.00, "quantity": 5}
];
    
shop_stock = load_date()

def stock_list(sr, stock_list, marksearch="", newquantity=0, newprice=0, reajusted_price=0):
    sum = 0
    global shop_stock
    if sr == "register":
       
       new_instrument = {
           "Mark":  marksearch,
           "price": newprice,
           "quantity": newquantity
       };
           
       shop_stock.append(new_instrument)
       print(f"Sucess! {marksearch} added to stock.")
       save(stock_list)
       return
    elif sr == "adjust":
        for instrument in stock_list:

            if instrument["price"]!=(instrument["price"]*reajusted_price):
                instrument["price"] = (instrument["price"]*reajusted_price)
        save(stock_list)
        return
    elif sr == "total value of stock":
        for instrument in stock_list:
            sum += instrument["price"]*instrument["quantity"];  
        print(f"The value total in stock {sum}");
        return
    elif sr == "sell":
        for instrument in stock_list:

            if instrument["Mark"] == marksearch:

                if instrument["quantity"]>0:
                    if instrument["quantity"]<newquantity:
                        print(f"Don't have this quantity, actually quantity {instrument['quantity']}")
                    else:
                        instrument["quantity"]-=newquantity
                        print(f"Sale realized!! Value:{instrument['price']*newquantity:.2f}")
                        print(f"The new stock of {marksearch}: {instrument['quantity']}")
                        save(stock_list)
                else:
                    print(f"The {marksearch} esgoted!!")

                return
        print("Instrument not encountered");


while True:
    print("\n--------MENU--------\n")
    action = input("Type: 'sell', 'register', 'adjust', 'total value of stock' or 'exit'\n")
    
    if action == "sell":
        mark = input("Insert the name of mark: ")
        quant = int(input("Insert the quantity: "))
        stock_list(action, shop_stock, mark, quant)

    elif action == "adjust":
        try:
            adjusting = float(input("Enter the price increase: "))
        except:
            print("Enter a number!!")
        else:
            stock_list(action, shop_stock, "", 0, 0, adjusting)

    elif action == "register":
        mark = input("Insert the name of mark: ")
        try:
            priceu = float(input("Insert the price: "))
            quant = int(input("Insert the quantity: "))
        except:
            print("Enter a number!!")
        else:
            stock_list(action, shop_stock, mark, quant, priceu)

    elif action == "total value of stock":
         stock_list(action, shop_stock)

    elif action == "exit":
        break
    else:
        print("Invalid command!!")