shop_stock = [
    {"Mark": "Tagima", "model": "Stratocaster", "price": 832.99, "quantity": 15},
    {"Mark": "Konig", "model": "Acoustic", "price": 500.00, "quantity": 12},
    {"Mark": "Yamaha", "model": "Pacifist", "price": 1320.00, "quantity": 5}
]

def stock_list(stock_list, marksearch):

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
        stock_list(shop_stock, mark )
