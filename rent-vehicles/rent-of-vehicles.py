import sqlite3

def conexao_load():
    return sqlite3.connect("rent_vehicles.db")

with conexao_load() as conexao:
    cursorcon = conexao.cursor()
    cursorcon.execute("""CREATE TABLE IF NOT EXISTS rent_vehicles(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    placa TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    valor_diaria FLOAT NOT NULL,
                    alugado BOOLEAN NOT NULL,
                    tipo_veiculo TEXT NOT NULL,
                    portas INTEGER,
                    capacidade_carga FLOAT
                )""")

class Veiculo:
    def __init__(self, placa: str, marca: str, diaria: float, alugado: bool):
        self.placa = placa
        self.marca = marca
        self.diaria = diaria
        self.alugado = alugado

    def alugar(self):
        match self.alugado:
            case False:
                return("O carro atualmente esta alugado")
            case True:
                return("O carro esta livre")
    