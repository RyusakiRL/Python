shop_stock = [
    {"Mark": "Tagima", "price": 832.99, "quantity": 15},
    {"Mark": "Konig", "price": 500.00, "quantity": 12},
    {"Mark": "Yamaha", "price": 1320.00, "quantity": 5}
]

def stock_list(sr, stock_list, marksearch, newquantity, newprice):
    if sr == "register" or sr == "cadaster":
       new_instrument = {
           "Mark":  marksearch,
           "price": newprice,
           "quantity": newquantity
       }

       shop_stock.append(new_instrument)
       print(f"Sucess! {marksearch} added to stock.")

    if sr == "sell":
        for instrument in stock_list:

            if instrument["Mark"] == marksearch:

                if instrument["quantity"]>0:
                    instrument["quantity"]-=1
                    print(f"Sale realized!! Value:{instrument['price']}")
                    print(f"The new stock of {marksearch}: {instrument['quantity']}")
                else:
                    print(f"The {marksearch} esgoted!!")

                return
    
        print("Instrument not encountered");


while True:
    sell = input("You want sell or cadaster the new product?\n")
    if sell == "sell":
        mark = input("Insert the name of mark\n")

        stock_list(sell, shop_stock, mark, 0, 0 )
    else:
        mark = input("Insert the name of mark\n")
        priceu = int(input("Insert the price\n"))
        quant = int(input("Insert the quantity\n"))
        stock_list(sell, shop_stock, mark, quant, priceu)

        
