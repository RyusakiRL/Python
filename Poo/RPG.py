personagens = []
class Character:
    def __init__(self, nome, energia=100):
        self.nome = nome
        self._energia = energia
    
    def descansar(self):
        self._energia = 100
        print("Descanso realizado com sucesso!!")

class Guerreiro(Character):
    def __init__(self, nome, energia=100, furia=0):
        super().__init__(nome, energia)
        self._furia = furia

    def ataque_pesado(self):
        if self._energia>=30:
            self._energia -= 30
            self._furia += 15
            print("Ataque devastador realizado!!")
            return True
        else:
            print(f"Voce nao tem energia o suficiente: Energia atual: [{self._energia}]")
            return False
        
    def descansar(self):
        self._furia = 0
        return super().descansar() 


class Corredor(Character):
    def __init__(self, nome, energia=100, stamina_extra=50):
        super().__init__(nome, energia)
        self._stamina_extra = stamina_extra
    
    def sprint_final(self):
        if self._energia>=40 and self._stamina_extra>10:
            self._energia -= 40
            self._stamina_extra -= 10
            print("Corrida final utilizada")
            return True
        else:
            print(f"Voce nao tem energia o suficiente: \nEnergia atual:[{self._energia}]  Stamina Extra: [{self._stamina_extra}]")
            return False
        
    def descansar(self):
        self._stamina_extra = 50
        return super().descansar()

def busca_personagem(nome, lista, acao):
    namen = None

    for buscas in lista:
        if buscas.nome == nome:
            namen = buscas
            break

    if namen!=None and acao == "at guer":
        namen.ataque_pesado()
    
    elif namen!=None and acao == "hab corr":
        namen.sprint_final()
    
    elif namen!=None and acao == "descansar":
        namen.descansar()

while True:    
    print("========================MENU DE PERSONAGEM========================")
    print("Escolha as opcoes abaixo:")
    action = str(input("[criar personagem] [usar ataque] [descansar] [sair]\n"))

    match action:
        case "criar personagem":
            criacao = str(input("Voce deseja criar um [guerreiro] ou [corredor]\n"))

            match criacao:
                case "guerreiro":
                    nome = str(input("Qual o nome do seu nobre guerreiro: "))
                    novo_guerreiro = Guerreiro(nome=nome)
                    personagens.append(novo_guerreiro)
                    print(f"Jovem guerreiro {nome} adicionado com sucesso")

                case "corredor":
                    nome = str(input("Qual o nome do seu velocista: "))
                    novo_corredor = Corredor(nome=nome)
                    personagens.append(novo_corredor)
                    print(f"O grande velocista {nome} foi adicionado com sucesso")
                
                case _:
                    print("Insert a valid command")
        
        case "usar ataque":
            classe = str(input("Qual a classe do seu personagem: "))

            match classe:
                case "guerreiro":
                    nomeguerreiro = str(input("Qual o nome do guerreiro: "))
                    busca_personagem(nome=nomeguerreiro, lista=personagens, acao="at guer")
                case "corredor":
                    nomecorredor = str(input("Qual o nome do corredor: "))
                    busca_personagem(nome=nomecorredor, lista=personagens, acao="hab corr")
        
        case "descansar":
            nomedesc = str(input("Qual o nome do personagem: "))
            busca_personagem(nome=nomedesc, lista=personagens,acao="descansar")
        
        case "sair":
            break

        case _:
            print("Invalid command")