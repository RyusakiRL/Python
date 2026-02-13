shop_stock = [
    {"Mark": "Tagima", "price": 832.00, "quantity": 15},
    {"Mark": "Konig", "price": 500.00, "quantity": 12},
    {"Mark": "Yamaha", "price": 1320.00, "quantity": 5}
]

def stock_list(sr, stock_list, marksearch, newquantity, newprice, reajusted_price):
    sum = 0
    if sr == "register":
       new_instrument = {
           "Mark":  marksearch,
           "price": newprice,
           "quantity": newquantity
       }

       shop_stock.append(new_instrument)
       print(f"Sucess! {marksearch} added to stock.")
    
    elif sr == "adjust":
        for instrument in stock_list:

            if instrument["price"]!=(instrument["price"]*reajusted_price):
                instrument["price"] = (instrument["price"]*reajusted_price)

    elif sr == "total value of stock":
        for instrument in stock_list:
            sum += instrument["price"]*instrument["quantity"];  
        print(f"The value total in stock {sum}");
    
    elif sr == "sell":
        for instrument in stock_list:

            if instrument["Mark"] == marksearch:

                if instrument["quantity"]>0:
                    instrument["quantity"]-=1
                    print(f"Sale realized!! Value:{instrument['price']:.2f}")
                    print(f"The new stock of {marksearch}: {instrument['quantity']}")
                else:
                    print(f"The {marksearch} esgoted!!")

                return
        print("Instrument not encountered");


while True:
    print("\n--------MENU--------\n")
    action = input("Type: 'sell', 'register', 'adjust' or 'total value of stock'\n")
    
    if action == "sell":
        mark = input("Insert the name of mark\n")
        stock_list(action, shop_stock, mark, 0, 0, 0 )

    elif action == "adjust":
        adjusting = float(input("Enter the price increase\n"))
        stock_list(action, shop_stock, "", 0, 0, adjusting)

    elif action == "register":
        mark = input("Insert the name of mark\n")
        priceu = float(input("Insert the price\n"))
        quant = int(input("Insert the quantity\n"))
        stock_list(action, shop_stock, mark, quant, priceu, 0)
    
    elif action == "total value of stock":
         stock_list(action, shop_stock, "", 0, 0, 0)

    else:
        print("Invalid command!!")