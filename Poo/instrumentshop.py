class Instrument():
    def __init__(self, mark, price, in_stock=True):
        self.marca = mark
        self.__price = price
        self.in_stock = in_stock
    
    def apply_discount(self, percent):
        self.__price = self.__price*(100-percent)

class eletric_guitar(Instrument):
    def __init__(self, mark, price, in_stock=True, string_number, tipo_captador):
        super().__init__(mark, price, in_stock)

        self.numeros_cordas = string_number
        self.tipo_captador = tipo_captador

    def tocar_com_distorcao(self):
        print("vuooom")

class batery(Instrument):
    def __init__(self, mark, price, in_stock=True, quantidades_pecas):
        super().__init__(mark, price, in_stock)
        
        self.quantidade_pecas = quantidades_pecas

    def montar(self):
        print(f"Montando as {self.quantidade_pecas} partes da bateria...")

all_instruments = []

while True:
    print("==================MAIN MENU==================")
    action = str(input("Type: 'eletric guitar', 'batery', 'other' or 'exit'"))