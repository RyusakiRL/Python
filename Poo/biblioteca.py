Biblioteca = []
Leitores = []

class Usuario:
    def __init__(self, nome, livro_em_posse= ""):
        self.nome = nome
        self.livroposse = livro_em_posse

    def retirarlivro(self, titulo):
        if self.livroposse!="":
            print(f"O {self.nome} agora esta em posse do livro {self.livroposse}")
        
        else:
            self.livroposse = titulo
            print(f"A pessoa {self.nome} retirou o livro [{titulo}] com sucesso!")
    
    def devolverlivro(self):
        if self.livroposse!= "":
            print(f"O livro {self.livroposse} foi devolvido!!")
            self.livroposse = ""
        else:
            print(f"{self.nome} nao pegou nenhum livro da biblioteca")

class Acervo:
    def __init__(self, titulo, descricao, autor, quantidade_livre, quantidade_ocupado=0):
        self.titulo = titulo
        self.descricao = descricao
        self.autor = autor
        self.quantidadel = quantidade_livre
        self.quantidadeo = quantidade_ocupado
    
    def __str__(self):
        return f"{self.titulo} (Disponível: {self.quantidadel} | Emprestado: {self.quantidadeo})"

    def emprestimo_reserva(self, acao):
        if self.quantidadel>0:
            try:
                self.quantidadel-=1
                self.quantidadeo+=1
                match acao:
                    case "realizar emprestimo":
                        print("Emprestimo de livro realizado com sucesso")
                    case "reservar":
                        print("Reserva de livro realizada com sucesso")
                    case "devolver livro":
                        print("Livro devolvido com sucesso")
            except ValueError:
                print("Livro esgotado")
    
    def livrodevolvido(self):
        self.quantidadel+=1
        self.quantidadeo-=1
    
while True:
    print("===================================MAIN MENU===================================")
    action = str(input("Escreva uma dessas ação:\n "
    "[reservar]  [realizar emprestimo] [adicionar livro] [adicionar usuario] [devolver livro] [listar] [sair]\n"
    ))
    
    if action == "adicionar livro":
        tituloL = str(input("Insira o titulo do livro: "))
        generoL = str(input("Insira a descricao do livro: "))
        autorL = str(input("Insira o nome do autor do livro: "))
        try:
            estoque = int(input("Insira a quantidade de livros: "))
            cervo = Acervo(tituloL, generoL, autorL, estoque)
            Biblioteca.append(cervo)
            print("O livro foi adicionado a biblioteca")

        except ValueError:
            print("Insira um valor inteiro")
    
    elif action == "adicionar usuario":
        nomeuser = str(input("Insira o nome do novo usuario: "))
        leitor = Usuario(nomeuser)

        Leitores.append(leitor)
        print("Usuario adicionado com sucesso")

    elif action == "reservar" or action=="realizar emprestimo":
        text = input(f"Qual o titulo, descricao ou autor do livro que voce deseja {action}: ")
        nome_pessoa = input(f"Qual o nome da pessoa que quer {action}: ")
        parameter = None
        for search in Biblioteca:
                       
            if search.titulo == text or search.autor == text or search.descricao == text:
                parameter = search
                break

        nome_parametro = None
        for searching in Leitores:
                
            if searching.nome == nome_pessoa:
                nome_parametro = searching
                break

        if parameter!= None and nome_parametro!= None:
            print("Name Encountered")
            parameter.emprestimo_reserva(action)
            nome_parametro.retirarlivro(parameter.titulo)
        
        else:
            print("Name don't encountered")
    
    elif action == "devolver livro":
        nome_pessoa = input("Insira o nome da pessoa quer devolver o livro: ")
        text = input("Qual o titulo, descricao ou autor do livro que sera devolvido: ")

        parameter = None              
        for search in Biblioteca:
                  
            if search.titulo == text or search.autor == text or search.descricao == text:
                parameter = search
                break

        nome_parametro = None            
        for searching in Leitores:
            
            if searching.nome == nome_pessoa:
                nome_parametro = searching
                break
        
        if parameter!= None and nome_parametro!= None:
            print("Name Encountered")
            parameter.livrodevolvido()
            nome_parametro.devolverlivro()
                
        else:
            print("Name don't encountered")
            
    elif action == "listar":
        ordem_decrescente = sorted(Biblioteca, key=lambda ocupado: (ocupado.quantidade0, ocupado.quantidadel), reverse=True)
        print("Os tres livros mais vistos da loja sao: ")
        print(ordem_decrescente[:3])
        ordem_crescente = sorted(Biblioteca, key=lambda livre: (livre.quantidadel, livre.quantidadeo))
        print("Os tres livros menos vistos")
        print(ordem_crescente[:3])

    elif action == "sair":
        break

    else:
        print("Invallid command!!!")

