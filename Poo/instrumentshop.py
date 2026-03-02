class Instrument():
    def __init__(self, mark, price, in_stock=True):
        self.marca = mark
        self._price = price
        self.in_stock = in_stock
    
    def apply_discount(self, percent):
        self._price = self._price*(1-(percent/100))
        print(f"Discount applied with sucess in {self.marca}: actual price R${self._price:.2f}")
class eletric_guitar(Instrument):
    def __init__(self, mark, price, in_stock=True, string_number=6, tipo_captador=""):
        super().__init__(mark, price, in_stock)

        self.numeros_cordas = string_number
        self.tipo_captador = tipo_captador

    def tocar_com_distorcao(self):
        print("vuooom")

class batery(Instrument):
    def __init__(self, mark, price, in_stock=True, quantidades_pecas=0):
        super().__init__(mark, price, in_stock)
        
        self.quantidade_pecas = quantidades_pecas

    def montar(self):
        print(f"Montando as {self.quantidade_pecas} partes da bateria...")

all_instruments = []

def searching(list, name_mark, actes, discount=0):
    nam = None
    for search in list:
        if search.marca == name_mark:
            nam = search
            break
    if nam!= None and actes == "dis":
        nam.apply_discount(discount)

    elif nam!= None and actes == "montar":
        nam.montar()
    else:
        print("Name don't encountered")

while True:
    print("==================MAIN MENU==================")
    action = str(input("Type: 'eletric guitar', 'batery', 'other', 'apply discount' or 'exit'\n"))

    if action == "other":
        marks = str(input("Type mark name: "))
        try:
            price = float(input("Insert the price: "))
            other_instrument = Instrument(marks, price)
            all_instruments.append(other_instrument)
        except ValueError:
            print("Insert a real value")
    
    elif action == "apply discount":
        name_mark = str(input("Insert the name mark of instrument: "))
        try:
            print("Insert the discount ", end="")
            discount = float(input())
            print(f"{discount}%")
            searching(all_instruments, name_mark, discount, "dis")
        
        except ValueError:
            print("Enter a real value")
    
    elif action == "eletric guitar":
        marks = str(input("Type mark name: "))
        captador = str(input("Insert the captator type: "))
        try:
            value = float(input("Type the guitar price: "))
            cords = int(input("Insert the quantity of strings: "))
            guitar_electric = eletric_guitar(marks, value, cords, captador)
            all_instruments.append(guitar_electric)
            guitar_electric.tocar_com_distorcao()

        except ValueError:
            print("Invallid value!!")
    
    elif action == "batery":
        action_batery = str(input("You want 'add' or 'set up': "))

        if action_batery == "add":
            mark_batery = str(input("Insert the mark of batery: "))
            try:
                pieces = int(input("Insert the quantity of batery pieces: "))
                prices = float(input("Insert the value: R$"))
                bateries = batery(mark_batery, prices, pieces)
                all_instruments.append(bateries)
            except ValueError:  
                print("Invalid value")
        
        elif action_batery == "set up":
            mark_batery = str(input("Insert the mark of batery: "))

            searching(all_instruments, mark_batery, "montar")


    elif action == "exit":
        break
        
