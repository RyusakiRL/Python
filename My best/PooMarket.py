ARCHIVE = "market_stock.json"

import json

class Product:
    def __init__(self, mark, quantity, price):
        self.mark = mark
        self.quantity = quantity
        self.price = price

    def sell(self, sell_quantity):
        if self.quantity>= sell_quantity:
            self.quantity-=sell_quantity
            return True
        else:
            print(f"Stock insufficient! We only have {self.quantity}.")
            return False
    
    def adjust(self, adjusting):
        self.price = self.price*adjusting

def save_data(saved_stock):
    data_to_save = []
    
    for product in saved_stock:
        data_to_save.append({
            "mark": product.mark,
            "quantity": product.quantity,
            "price": product.price
            })
    with open(ARCHIVE, "w") as file:
        json.dump(data_to_save, file, indent=4)


def load_data():
    try:
        with open(ARCHIVE, "r") as file:
            data_json = json.load(file)

            reconstructed_stock = []
            
            for item in data_json:
                news_product = Product(item["mark"], item["quantity"], item["price"])
                reconstructed_stock.append(news_product)

                return reconstructed_stock
    except FileNotFoundError:

        return []

stock = load_data()

while True:
    print("==================\MENU/==================")
    act = input("Type: 'register', 'sell', 'adjust' or 'exit': ")

    if act == "register":
        marks = input("Type the mark: ")
        try:
            quant = int(input("Type quantity: "))
            price = float(input("Type the value: "))

            new_product = Product(marks, quant, price)
            stock.append(new_product)            
            save_data(stock)

        except ValueError:
            print("Invalid number!!")

        else:
            print(f"{marks} registered with sucess!!")
        
    elif act == "sell":
        marks = input("Type the mark: ")
        try:
            quant = int(input("Type the quantity: "))
            
            found = False
            for products in stock:
                if products.mark == marks:
                    found = True

                    sucess = products.sell(quant)
                    save_data(stock)

                    if sucess:
                        print(f"{marks} was sold with sucess!!\n Total value: R${products.price*quant}")
                    break

            if not found:
                print(f"This marks {marks} don't exists")

        except ValueError:
            print("Invalid number!!")

    elif act == "adjust":
        marks = input("Type the mark: ")
        try:
            adjusting = float(input("Enter the adjust: "))

            found = False
            for product in stock:
                if product.mark == marks:
                    found = True

                    product.adjust(adjusting)
                    save_data(stock)
                if found:
                    print(f"The new price of {marks} is R${product.price:.2f}")                
                break

            if not found:
                print(f"This marks {marks} don't exists")

        except ValueError:
            print("Invalid number!!")

    elif act == "exit":
        break