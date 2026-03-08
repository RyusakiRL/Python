"""
Módulo de gerenciamento de frota espacial.
Este sistema controla o combustível, integridade e viagens de sondas e cargueiros.
"""
import sqlite3

SONDA = 1
NAVECARGA = 2
COMBUSTIVEL = 100.0
INTEGRIDADE = 100.0

def conexao():
    """conexao com o banco de dados chamado agencia_espacial.db"""
    return sqlite3.connect("agencia_espacial.db")


def criar_agencia():
    """Criação da tabela de agência espacial, caso ela ainda não exista."""
    with conexao() as cursor_con:
        cursorcon = cursor_con.cursor()

        cursorcon.execute("""CREATE TABLE IF NOT EXISTS agencia_espacial(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL UNIQUE,
                                combustivel FLOAT,
                                integridade FLOAT,
                                tipo INTEGER)""")

criar_agencia()

class Espaconave:
    """Classe base para todas as espaçonaves, contendo atributos comuns e métodos abstratos."""
    def __init__(self, nome_nave: str, combustivel_nave: float, integridade_nave: float):
        self.nome = nome_nave
        self._combustivel = combustivel_nave
        self._integridade = integridade_nave

    @property
    def combustivel(self):
        """Retorna o nível atual de combustível da espaçonave."""
        return self._combustivel

    @property
    def integridade(self):
        """Retorna o nível atual de integridade da espaçonave."""
        return self._integridade

    def viajar(self, distancia_viajar):
        """Método abstrato para realizar uma viagem, deve ser implementado pelas classes filhas."""
        raise NotImplementedError("A classe filha deve sobrescrever o metodo viajar!")

class Sondaexploratoria(Espaconave):
    """Classe para sondas, com um método de viagem que calcula os gastos de combustível da mesma."""
    def viajar(self, distancia_viajar):
        gastos = distancia_viajar*1.5
        danos = distancia_viajar*0.5
        if self._integridade<50:
            print("Integridade muito abaixo, nao sera possivel o voo")
            return False
        elif self._combustivel >= gastos:
            print("Voo realizado com sucesso")
            self._combustivel -= gastos
            self._integridade -= danos
            return True
        else:
            print("Combustivel insuficiente")
            return False
    def reparar(self):
        """Metodo para reparar a sonda, aumentando a integridade ate o limite de 100."""
        if self._integridade < 100:
            self._integridade = 100
            print("Sonda reparada com sucesso!")
        else:
            print("A sonda ja esta em perfeitas condicoes, nao e necessario reparar.")

class Navecargueiro(Espaconave):
    """classe para Nave cargueiro, que calcula viagem e abastecimento."""
    def abastecer(self):
        """Metodo para reabastecer a nave, aumentando o combustível ate o limite de 100."""
        if self._combustivel < 100:
            self._combustivel = 100
            print("Nave reabastecida com sucesso!")
        else:
            print("O tanque ja esta cheio, nao e necessario reabastecer.")
    def viajar(self, distancia_viajar):
        gastos = distancia_viajar*4
        danos = distancia_viajar*0.5
        if self._integridade<50:
            print("Integridade muito abaixo, nao sera possivel o voo")
            return False
        elif self._combustivel >= gastos:
            print("Voo realizado com sucesso")
            self._combustivel -= gastos
            self._integridade -= danos
            return True
        else:
            print("Combustivel insuficiente")
            return False
def save_data():
    """Função para salvar os dados das espaçonaves no banco de dados."""
    lista_naves = []

    with conexao() as cursor_connect:
        cursor = cursor_connect.cursor()

        cursor.execute("""SELECT nome, combustivel, integridade, tipo FROM agencia_espacial""")
        resultados = cursor.fetchall()
        for informacoes in resultados:
            nome_infor, combustivel_infor, integridade_espaco, tipo = informacoes
            match tipo:
                case 1:
                    sondagem = Sondaexploratoria(nome_nave=nome_infor,
                                                 combustivel_nave=combustivel_infor,
                                                 integridade_nave=integridade_espaco)
                    lista_naves.append(sondagem)
                case 2:
                    navecarga = Navecargueiro(nome_nave=nome_infor,
                                              combustivel_nave=combustivel_infor,
                                              integridade_nave=integridade_espaco)
                    lista_naves.append(navecarga)

    return lista_naves

lista_todas_naves = save_data()

while True:
    print("=================MAIN MENU=================")
    print("Escolha uma das opcoes abaixo:")
    ACAO = int(input
               ("[1] - Criar Sonda Exploratoria [2] - Criar Nave Cargueiro"
                " [3] - lancar missao [4] - Reabastecer Nave [5] - Reparar Nave [6] - Sair\n"))

    match ACAO:
        case 1:
            NOME_SONDA = str(input("Digite o nome da sonda exploratoria: "))
            with conexao() as cursor2:
                cursorcon2 = cursor2.cursor()
                cursorcon2.execute("""SELECT nome FROM agencia_espacial WHERE nome = ?""",
                                   (NOME_SONDA,))
                if cursorcon2.fetchone():
                    print("O nome da sonda ja existe, por favor escolha outro nome.")
                    continue

                cursorcon2.execute("""INSERT INTO agencia_espacial
                                   (nome, combustivel, integridade, tipo)
                                    VALUES (?, ?, ?, ?)""",
                                    (NOME_SONDA, COMBUSTIVEL, INTEGRIDADE, SONDA))
                print("Sonda exploratoria criada com sucesso!")
                lista_todas_naves.append(Sondaexploratoria(nome_nave=NOME_SONDA,
                                                            combustivel_nave=COMBUSTIVEL,
                                                            integridade_nave=INTEGRIDADE))
        case 2:
            NOME_NAVECARGA = str(input("Digite o nome da nave cargueiro: "))

            with conexao() as cursor3:
                cursorcon3 = cursor3.cursor()
                cursorcon3.execute("""SELECT nome FROM agencia_espacial WHERE nome = ?""",
                                   (NOME_NAVECARGA,))
                if cursorcon3.fetchone():
                    print("O nome da nave cargueiro ja existe, por favor escolha outro nome.")
                    continue
                cursorcon3.execute("""INSERT INTO agencia_espacial
                                   (nome, combustivel, integridade, tipo)
                                    VALUES (?, ?, ?, ?)""",
                                    (NOME_NAVECARGA, COMBUSTIVEL, INTEGRIDADE, NAVECARGA))
                print("Nave cargueiro criada com sucesso!")
                lista_todas_naves.append(Navecargueiro(nome_nave=NOME_NAVECARGA,
                                                        combustivel_nave=COMBUSTIVEL,
                                                        integridade_nave=INTEGRIDADE))
        case 3:
            if not lista_todas_naves:
                print("Nenhuma nave disponivel para lancar missao.")
                continue
            print("Naves disponiveis para lancar missao:")
            for idx, nave in enumerate(lista_todas_naves, start=0):
                if isinstance(nave, Sondaexploratoria):
                    print(f"{idx}. Sonda de exploracao: {nave.nome} "
                          f"(Combustivel: {nave.combustivel}, Integridade: {nave.integridade})")       
                else:
                    print(f"{idx}. Nave cargueiro: {nave.nome} "
                          f"(Combustivel: {nave.combustivel}, Integridade: {nave.integridade})")
            try:
                escolha_nave = int(input("Escolha o numero da nave para lancar a missao: "))
                if 0 <= escolha_nave < len(lista_todas_naves):
                    nave_escolhida = lista_todas_naves[escolha_nave]
                    distancia = float(input("Digite a distancia da missao: "))
                    nave_escolhida.viajar(distancia)
                    with conexao() as cursor4:
                        cursorcon4 = cursor4.cursor()
                        cursorcon4.execute("""UPDATE agencia_espacial
                                            SET combustivel = ?, integridade = ?
                                            WHERE nome = ?""",
                                            (nave_escolhida.combustivel,
                                            nave_escolhida.integridade,
                                            nave_escolhida.nome))
                else:
                    print("Escolha invalida. Por favor, tente novamente.")
            except ValueError:
                print("Entrada invalida. Por favor, digite um numero valido.")

        case 4:
            with conexao() as cursor5:

                cursorcon5 = cursor5.cursor()
                cursorcon5.execute("""SELECT nome, combustivel
                                   FROM agencia_espacial WHERE tipo = ?""",
                                   (NAVECARGA,))
                naves_carga = cursorcon5.fetchall()
                if not naves_carga:
                    print("Nenhuma nave cargueiro disponivel para reabastecer.")
                    continue
                print("Naves cargueiro disponiveis para reabastecer:")
                for idx, (nome, combustivel) in enumerate(naves_carga, start=0):
                    print(f"{idx}. {nome} (Combustivel: {combustivel})")
                try:
                    escolha_nave = int(input("Escolha o numero da nave para reabastecer: "))
                    if 0 <= escolha_nave < len(naves_carga):
                        nome_nave_escolhida = naves_carga[escolha_nave][0]
                        nave_escolhida = next((nave for nave in lista_todas_naves
                                            if nave.nome == nome_nave_escolhida), None)
                        if isinstance(nave_escolhida, Navecargueiro):
                            nave_escolhida.abastecer()
                            cursorcon5.execute("""UPDATE agencia_espacial
                                            SET combustivel = ?
                                            WHERE nome = ?""",
                                            (nave_escolhida.combustivel,
                                            nave_escolhida.nome))
                    else:
                        print("Escolha invalida. Por favor, tente novamente.")
                except ValueError:
                    print("Entrada invalida. Por favor, digite um numero valido.")
        case 5:
            with conexao() as cursor6:
                cursorcon6 = cursor6.cursor()
                cursorcon6.execute("""SELECT nome, integridade
                                   FROM agencia_espacial WHERE tipo = ?""",
                                   (SONDA,))
                naves_disponiveis = cursorcon6.fetchall()
                if not naves_disponiveis:
                    print("Nenhuma nave disponivel para reparar.")
                    continue
                print("Naves disponiveis para reparar:")
                for idx, (nome, integridade) in enumerate(naves_disponiveis, start=0):
                    print(f"{idx}. {nome} (Integridade: {integridade})")
                try:
                    escolha_nave = int(input("Escolha o numero da nave para reparar: "))
                    if 0 <= escolha_nave < len(naves_disponiveis):
                        nome_nave_escolhida = naves_disponiveis[escolha_nave][0]
                        nave_escolhida = next((nave for nave in lista_todas_naves
                                            if nave.nome == nome_nave_escolhida), None)
                        if nave_escolhida:
                            nave_escolhida.reparar()
                            cursorcon6.execute("""UPDATE agencia_espacial
                                            SET integridade = ?
                                            WHERE nome = ?""",
                                            (nave_escolhida.integridade,
                                        nave_escolhida.nome))
                    else:
                        print("Escolha invalida. Por favor, tente novamente.")
                except ValueError:
                    print("Entrada invalida. Por favor, digite um numero valido.")
        case 6:
            print("Encerrando o programa!")
            break
        case _:
            print("Opcao invalida, por favor escolha uma opcao valida.")
