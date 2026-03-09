import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # 1. Importamos o criador de moldes

app = FastAPI()

def conexao():
    """Conecta com o seu arquivo local do SQLite."""
    return sqlite3.connect("agencia_espacial.db")
# --- SEUS MOLDES DE DADOS (Pydantic) ---

class NaveInput(BaseModel):
    """Molde de segurança: define o que a internet precisa enviar."""
    nome: str
    combustivel: float = 100.0  # Se o usuário não enviar, assume 100.0
    integridade: float = 100.0
    tipo: int # Ex: 1 para Sonda, 2 para Cargueiro


# --- SUAS ROTAS (Endpoints) ---

@app.get("/")
def pagina_inicial():
    return {"mensagem": "Olá, Universo! Minha primeira API está no ar."}

@app.get("/nave/{nome_da_nave}")
def saudar_nave(nome_da_nave: str):
    return {"status": "sucesso", "mensagem": f"Bem-vinda de volta à base, {nome_da_nave}!"}

# 2. A ROTA NOVA: Usamos POST para CRIAR dados
@app.post("/nave")
def criar_nave(dados_da_nave: NaveInput):
    """
    Cria uma nave e salva permanentemente no banco de dados SQLite.
     - O FastAPI já valida e transforma o JSON recebido em um objeto 'NaveInput
    """
    # A variável 'dados_da_nave' já chega aqui mastigada e validada!

    with conexao() as conn:
        cursor = conn.cursor()
        # Criar a tabela se não existir (pode ser feito uma vez, mas é seguro deixar aqui)
        cursor.execute("""SELECT nome FROM agencia_espacial WHERE nome= ?""", (dados_da_nave.nome,))
        # Inserir os dados da nave, mas primeiro verificar se já existe uma nave com o mesmo nome
        if cursor.fetchone():
            raise HTTPException(status_code=400, 
                                detail=f"Operação negada: A nave '{dados_da_nave.nome}' já existe na agência!")
        
        cursor.execute("""
            INSERT INTO agencia_espacial(nome, combustivel, integridade, tipo)
            VALUES (?, ?, ?, ?)
        """, (dados_da_nave.nome, dados_da_nave.combustivel, dados_da_nave.integridade, dados_da_nave.tipo))
    
    return {
        "status": "sucesso",
        "mensagem": f"A nave '{dados_da_nave.nome}' foi salva permanentemente no banco de dados!"
    }

@app.get("/naves")
def listar_naves():
    """Busca todas as naves cadastradas no banco de dados e retorna uma lista JSON."""
    with conexao() as conn:
        cursor = conn.cursor()
        
        # Buscamos todos os dados da tabela
        cursor.execute("SELECT id, nome, combustivel, integridade, tipo FROM agencia_espacial")
        resultados = cursor.fetchall()
        
        # Criamos uma lista vazia para guardar as naves formatadas
        frota = []
        
        # Transformamos cada tupla do SQLite em um dicionário bem organizado
        for linha in resultados:
            id_nave, nome, combustivel, integridade, tipo = linha
            
            # Um pequeno 'toque de mestre' para o Front-End:
            nome_tipo = "Sonda Exploratória" if tipo == 1 else "Nave Cargueiro" if tipo == 2 else "Desconhecido"
            
            frota.append({
                "id": id_nave,
                "nome": nome,
                "combustivel": combustivel,
                "integridade": integridade,
                "tipo_codigo": tipo,
                "tipo_nome": nome_tipo
            })
            
    return {
        "status": "sucesso", 
        "total_naves": len(frota), 
        "frota": frota
    }

@app.put("/nave/{nome_da_nave}/abastecer")
def abastecer_nave(nome_da_nave: str):
    """Reabastece o tanque de um Cargueiro de volta para 100.0."""
    with conexao() as conn:
        cursor = conn.cursor()
        
        # 1. A LANTERNA: A nave existe no banco de dados?
        cursor.execute("SELECT tipo, combustivel FROM agencia_espacial WHERE nome = ?", (nome_da_nave,))
        nave_encontrada = cursor.fetchone()
        
        if not nave_encontrada:
            raise HTTPException(status_code=404, detail=f"Erro 404: Nave '{nome_da_nave}' não encontrada no radar.")
            
        tipo_nave, combustivel_atual = nave_encontrada
        
        # 2. A REGRA DE NEGÓCIO: Sondas não podem abastecer, lembra do seu projeto?
        if tipo_nave == 1:
            raise HTTPException(
                status_code=400, 
                detail="Operação negada: Sondas Exploratórias não possuem tanque de reabastecimento comercial."
            )
            
        if combustivel_atual >= 100.0:
            return {"status": "aviso", "mensagem": f"O tanque da nave '{nome_da_nave}' já está em 100%!"}
            
        # 3. A CHAVE DE FENDA: Atualizando o dado de verdade (O comando UPDATE)
        cursor.execute("UPDATE agencia_espacial SET combustivel = 100.0 WHERE nome = ?", (nome_da_nave,))
        
        # Como estamos usando o 'with conexao()', o Python já faz o 'commit' (salva de verdade) aqui.
        
    return {
        "status": "sucesso",
        "mensagem": f"A nave cargueiro '{nome_da_nave}' foi reabastecida com sucesso para sua próxima missão!"
    }

@app.delete("/nave/{nome_da_nave}/aposentar")
def aposentar_nave(nome_da_nave: str):
    """Aposenta (deleta) uma nave permanentemente do banco de dados."""
    
    with conexao() as conn:
        cursor = conn.cursor()
        
        # 1. A LANTERNA: A nave realmente existe antes de tentarmos apagar?
        cursor.execute("SELECT nome FROM agencia_espacial WHERE nome = ?", (nome_da_nave,))
        if not cursor.fetchone():
            raise HTTPException(
                status_code=404, 
                detail=f"Erro 404: Operação negada. A nave '{nome_da_nave}' não consta nos nossos registros."
            )
            
        # 2. A MARRETA: O comando SQL que apaga a linha inteira do banco
        cursor.execute("DELETE FROM agencia_espacial WHERE nome = ?", (nome_da_nave,))
        
        # O 'with' garante o commit, efetivando a exclusão no arquivo .db
        
    return {
        "status": "sucesso",
        "mensagem": f"A nave '{nome_da_nave}' foi aposentada e removida da frota oficial!"
    }