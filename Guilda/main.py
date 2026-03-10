"""Sistema de Gerenciamento de Mercenários e Contratos para uma Guilda"""
import sqlite3
from typing import Optional, Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

aplicacao = FastAPI()

def conexao_guilda():
    """conecta com o arquivo SQL mercenarios"""
    return sqlite3.connect("guilda.db")

with conexao_guilda() as conexao1:
    cursorcon = conexao1.cursor()
    cursorcon.execute("""CREATE TABLE IF NOT EXISTS mercenarios(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        rank TEXT NOT NULL,
                        status BOOLEAN NOT NULL
                        )""")
    cursorcon.execute("""CREATE TABLE IF NOT EXISTS contratos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        alvo TEXT NOT NULL,
                        recompensa FLOAT NOT NULL,
                        status TEXT NOT NULL,
                        mercenario_id INTEGER,
                        FOREIGN KEY (mercenario_id) REFERENCES mercenarios (id)                      
                        
                        
                        )""")

class Mercenario(BaseModel):
    """Cria o modelo de mercenário para a guilda."""
    nome: str
    rank: Literal["F", "E", "D", "C", "B", "A", "S"]
    status: bool

class Contrato(BaseModel):
    """Cria o modelo de contrato para os mercenarios."""
    alvo: str
    recompensa: float
    status: Literal["aberto", "em andamento"] = "aberto"
    mercenario_id: Optional[int] = None

@aplicacao.post("/mercenarios")
def criar_mercenario(mercenario_criado: Mercenario):
    """Cria um novo mercenário e o adiciona à guilda."""
    with conexao_guilda() as conexao2:
        cursor2 = conexao2.cursor()
        cursor2.execute("SELECT * FROM mercenarios WHERE nome = ?", (mercenario_criado.nome,))
        if cursor2.fetchone() is not None:
            raise HTTPException(status_code=400, detail="Mercenário já existe.")
        else:
            cursor2.execute("""INSERT INTO mercenarios (nome, rank, status)
                            VALUES (?, ?, ?)""",
                            (mercenario_criado.nome,
                            mercenario_criado.rank,
                            mercenario_criado.status))

    return {"mensagem": "Mercenário criado com sucesso!"}

@aplicacao.post("/contratos")
def criar_contrato(contrato_criado: Contrato):
    """Cria um novo contrato e o associa a um mercenário existente."""
    with conexao_guilda() as conexao3:
        cursor3 = conexao3.cursor()
        cursor3.execute("""INSERT INTO contratos (alvo, recompensa, status, mercenario_id)
                        VALUES (?, ?, ?, ?)""",
                        (contrato_criado.alvo,
                         contrato_criado.recompensa,
                         "aberto",
                         contrato_criado.mercenario_id))
    return {"mensagem": "Contrato criado com sucesso!"}


@aplicacao.get("/contratos/abertos")
def listar_contratos():
    """Lista todos os contratos cadastrados na guilda em aberto."""
    with conexao_guilda() as conexao4:
        cursor4 = conexao4.cursor()
        cursor4.execute("SELECT * FROM contratos WHERE status = 'aberto'")
        contratos_abertos = []
        for contrato in cursor4.fetchall():
            contratos_abertos.append({
                "id": contrato[0],
                "alvo": contrato[1],
                "recompensa": contrato[2],
                "status": contrato[3],
                "mercenario_id": contrato[4]
            })
    return {"contratos": contratos_abertos}

@aplicacao.put("/contratos/{id_contrato}/aceitar/{id_mercenario}")
def validacao_contrato(id_contrato: int, id_mercenario: int):
    """Permite que um mercenário aceite um contrato, apos verificacao."""
    with conexao_guilda() as conexao6:
        cursor6 = conexao6.cursor()
        cursor6.execute("SELECT * FROM contratos WHERE id = ?", (id_contrato,))
        contrato = cursor6.fetchone()
        if contrato is None:
            raise HTTPException(status_code=404, detail="Contrato não encontrado.")
        if contrato[3] != "aberto":
            raise HTTPException(status_code=400, detail="Contrato já está em andamento.")
        cursor6.execute("SELECT * FROM mercenarios WHERE id = ?", (id_mercenario,))
        mercenario = cursor6.fetchone()
        if mercenario is None:
            raise HTTPException(status_code=404, detail="Mercenário não encontrado.")
        if not mercenario[3]:  # Verifica se o mercenário está disponível
            raise HTTPException(status_code=400, detail="Mercenário não está disponível.")
        cursor6.execute("""UPDATE contratos SET status = ?, mercenario_id = ? WHERE id = ?""",
                        ("em andamento", id_mercenario, id_contrato))

    return {"mensagem": "Contrato aceito com sucesso!"}

@aplicacao.delete("/mercenarios/{id_to_del}")
def deletar_mercenario(id_to_del: int):
    """Deleta um mercenário da guilda."""
    with conexao_guilda() as conexao7:
        cursor7 = conexao7.cursor()
        cursor7.execute("SELECT id FROM mercenarios WHERE id = ?", (id_to_del,))
        if cursor7.fetchone() is None:
            raise HTTPException(status_code=404, detail="Mercenário não encontrado.")
        cursor7.execute("SELECT id FROM contratos WHERE mercenario_id = ? AND status = ?",
            (id_to_del, "em andamento"))
        if cursor7.fetchone() is not None:
            raise HTTPException(status_code=400,
                                detail=
                                "Mercenário não pode ser deletado, possui contratos em andamento.")
        cursor7.execute("DELETE FROM mercenarios WHERE id = ?", (id_to_del,))
    return {"mensagem": "Mercenário deletado com sucesso!"}
