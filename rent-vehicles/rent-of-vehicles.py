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
        self._placa = placa
        self._marca = marca
        self._diaria = diaria
        self._alugado = alugado

    def alugar(self):
        match self._alugado:
            case False:
                print("Aluguel realizado com sucesso!")
                self._alugado = True
            case True:
                return True

    def devolver_veiculo(self):
        match self._alugado:
            case True:
                print("Veiculo devolvido com sucesso")
                self._alugado = False
            case False:
                return False
class Carro(Veiculo):
    def __init__(self, placa, marca, diaria, alugado, portas:int):
        super().__init__(placa, marca, diaria, alugado)
        self._portas = portas
    
    def calcular_preco(self, dias_alugado: int):
        preco_total = dias_alugado*self._diaria
        print(f"O valor ficou R${preco_total:.2f}")

class Caminhao(Veiculo):
    def __init__(self, placa, marca, diaria, alugado, capacidade_carga: float):
        super().__init__(placa, marca, diaria, alugado)
        self._capacidade_carga = capacidade_carga
    
    def calcular_preco(self, dias_alugado: int):
        preco_total = dias_alugado*self._diaria
        print(f"O valor ficou R${preco_total:.2f}")

def save():
    with conexao_load() as conexao:
        cursorcon = conexao.cursor()

        cursorcon.execute("""SELECT placa, marca, valor_diaria, alugado, tipo_veiculo, portas, capacidade_carga FROM rent_vehicles""")
        informacoes = cursorcon.fetchall()

        lista_veiculos_empresa = []

        for listando in informacoes:
            placa, marca, valor_diaria, alugado, tipo_veiculo, portas, capacidade_carga = listando

            match tipo_veiculo:
                case "carro":
                    match alugado:
                        case 0:
                            classe_de_carro = Carro(placa=placa, marca=marca, diaria=valor_diaria, alugado=False, portas=portas)
                            lista_veiculos_empresa.append(classe_de_carro)
                        case 1:
                            classe_de_carro = Carro(placa=placa, marca=marca, diaria=valor_diaria, alugado=True, portas=portas)
                            lista_veiculos_empresa.append(classe_de_carro)

                case "caminhao":
                    match alugado:
                        case 0:
                            classe_de_caminhao = Caminhao(placa=placa, marca=marca, diaria=valor_diaria, alugado=False, capacidade_carga=capacidade_carga)
                            lista_veiculos_empresa.append(classe_de_caminhao)
                        case 1:
                            classe_de_caminhao = Caminhao(placa=placa, marca=marca, diaria=valor_diaria, alugado=True, capacidade_carga=capacidade_carga)
                            lista_veiculos_empresa.append(classe_de_caminhao)

    return lista_veiculos_empresa

def busca_placa(name, list):
    existence = None
    for searching in list:
        if searching._placa == name:
            existence = searching
            return existence
    if existence == None:
        return None

load_savedata = save()

while True:
    print("====================================================================MAIN MENU====================================================================")
    acao = str(input("Escolha uma das opcoes abaixo:\n [cadastrar novo veiculo] [ver veiculos disponiveis] [alugar veiculo] [devolver veiculo] [sair]\n"))

    match acao.lower():
        case "cadastrar novo veiculo":
            tipagem_veiculo = str(input("O veiculo registrado seria um caminhao ou um carro: "))
            
            while tipagem_veiculo.lower()!="caminhao" and tipagem_veiculo.lower()!="carro":
                tipagem_veiculo = str(input("Nao atendemos esse tipo de veiculo no servidor, escolha apenas entre [carro] ou [caminhao]: "))
            
            match tipagem_veiculo:
                case "caminhao":
                    placa_do_caminhao = str(input("Insira a numeracao da placa: "))

                    cursorcon.execute("SELECT placa FROM rent_vehicles WHERE placa=?", (placa_do_caminhao,))
                    existencia_placa = cursorcon.fetchone()

                    if existencia_placa==None:
                        marca_caminhao = str(input("Qual o nome da marca: "))
                        try:
                            valor_da_diaria = float(input("Insira o valor do uso por dia: R$"))
                            capacidade_de_carga = float(input("Insira a capacidade de carga em kg: "))

                            with conexao_load() as conexao:
                                cursorcon = conexao.cursor()
                                cursorcon.execute("""INSERT INTO rent_vehicles(placa, marca, valor_diaria, alugado, tipo_veiculo, capacidade_carga)
                                                  VALUES(?, ?, ?, ?, ?, ?)""", 
                                                  (placa_do_caminhao, marca_caminhao, valor_da_diaria, 0, "caminhao", capacidade_de_carga))
                            novo_caminhao = Caminhao(placa=placa_do_caminhao, marca=marca_caminhao, diaria=valor_da_diaria, alugado=False, capacidade_carga=capacidade_de_carga)
                            load_savedata.append(novo_caminhao)

                            print("Cadastro realizado com sucesso")
                        except ValueError:
                            print("Insira um numero real")
                    else:
                        print("Ja existe uma placa com mesma numeracao")
                
                case "carro":
                    placa_do_carro = str(input("Insira a numeracao da placa: "))

                    cursorcon.execute("SELECT placa FROM rent_vehicles WHERE placa=?", (placa_do_carro,))
                    existencia_placa = cursorcon.fetchone()

                    if existencia_placa==None:
                        marca_carro = str(input("Qual o nome da marca: "))
                        try:
                            valor_da_diaria = float(input("Insira o valor do uso por dia: R$"))
                            quantidade_portas = int(input("Insira a capacidade de carga em kg: "))

                            with conexao_load() as conexao:
                                cursorcon = conexao.cursor()
                                cursorcon.execute("""INSERT INTO rent_vehicles(placa, marca, valor_diaria, alugado, tipo_veiculo, portas)
                                                  VALUES(?, ?, ?, ?, ?, ?)""", 
                                                  (placa_do_carro, marca_carro, valor_da_diaria, 0, "carro", quantidade_portas))
                            novo_carro = Carro(placa=placa_do_carro, marca=marca_carro, diaria=valor_da_diaria, alugado=False, portas=quantidade_portas)
                            load_savedata.append(novo_carro)
                                
                            print("Cadastro realizado com sucesso")

                        except ValueError:
                            print("Insira um numero real")
                    else:
                        print("Ja existe uma placa com mesma numeracao")
        
        case "ver veiculos disponiveis":
            existencia_disponivel = False
            for veiculos in load_savedata:
                match veiculos._alugado:
                    case False:
                        existencia_disponivel = True
                        print("------------------------------------------------------------------------------------")
                        print(f"O veiculo {veiculos._marca} de placa {veiculos._placa} esta disponivel")
            
            if not existencia_disponivel:
                print("Nao existe nenhum carro disponivel para aluguel no estoque")
                    
        case "alugar veiculo":
            numero_placa = str(input("Insira a numeracao da placa: "))

                
            resultado = busca_placa(name=numero_placa, list=load_savedata)
            if resultado!= None:
                if resultado._alugado == True:
                    print("Veiculo atualmente esta sendo usado!")
                    
                else:
                    with conexao_load() as conexao:
                        cursorcon = conexao.cursor()
                        cursorcon.execute("""UPDATE rent_vehicles
                                            SET alugado = ?
                                            WHERE placa = ?""",
                                            (1, numero_placa,))
                    resultado.alugar()
            else:
                print("Placa nao encontrada")

        case "devolver veiculo":
            numero_placa = str(input("Insira a numeracao da placa: "))
            while True:
                    
                resultado = busca_placa(name=numero_placa, list=load_savedata)
                
                if resultado!= None:
                    if resultado._alugado != False:
                        try:
                            valor_total_aluguel = int(input("Quantos dias a pessoa ficou com o veiculo: "))
                            with conexao_load() as conexao:
                                cursorcon = conexao.cursor()
                                cursorcon.execute("""UPDATE rent_vehicles
                                                    SET alugado = ?
                                                    WHERE placa = ?""",
                                                    (0, numero_placa,))
                            resultado.calcular_preco(dias_alugado=valor_total_aluguel)
                            resultado.devolver_veiculo()
                        except ValueError:
                            print("Insira um numero valido")
                        break

                    elif resultado._alugado == False:
                        numero_placa = str(input("Veiculo nao estava sendo alugado, deseja [voltar] ou insira outra numeracao de placa: "))
                        if numero_placa == "voltar":
                            break
                elif resultado == None:
                    numero_placa = str(input("A placa nao existe, insira outra numeracao de placa ou [voltar]:"))
                    if numero_placa == "voltar":
                        break
        case "sair":
            break
        case _:
            print("Invallid command")