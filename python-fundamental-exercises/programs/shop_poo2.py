class Instrument:
    def __init__(self, mark, price, quantity):
        self.mark = mark
        self.price = price
        self.quantity = quantity
   
    def sell(self, sell_quantity):    

        if self.quantity>=sell_quantity:
            self.quantity-=sell_quantity

            print(f"Sucess! {sell_quantity} {self.mark}(s) sold.")
        else:
            print("Stock insufficient!")
    
    def adjust(self, adjust_price):
        self.price = self.price*adjust_price

product1 = Instrument("Yamaha", 1750, 12)
product2 = Instrument("Tagima", 1100, 10)

act = input("Type: 'sell' or 'adjust': ")

if act == "sell":
    try:
        quantities = int(input("Insert the sell quantity:\n "))
        product1.sell(quantities)
        print(f"Atual stock of {product1.mark}: {product1.quantity}")

    except ValueError:
        print("Enter a number!!")

elif act == "adjust":
    try:
        adjusting = int(input("Insert the adjust:\n "))
        product1.adjust(adjusting)
        print(f"Atual stock of {product1.mark}: R${product1.price}")

    except ValueError:
        print("Enter a number!!")