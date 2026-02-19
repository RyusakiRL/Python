class Instrument:
    def __init__(self, mark, price, quantity):
        self.mark = mark
        self.price = price
        self.quantity = quantity


product1 = Instrument("Yamaha", 1200, 12)
product2 = Instrument("Yongos", 3200, 3)

print(f"We have {product1.quantity} guitar of mark {product1.mark} with price R${product1.price}")