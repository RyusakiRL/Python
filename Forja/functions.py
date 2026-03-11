"""Funcoes do sistema de cadastro de aventureiros e armas."""

from fastapi import HTTPException
from models import Aventureiro, Arma
from database import conexao


def criar_aventureiro(aventureiro: Aventureiro):
    """Endpoint para criar um novo aventureiro.
    - Verifica se o aventureiro já existe no banco de dados."""
    with conexao() as conn1:
        cursor1 = conn1.cursor()
        cursor1.execute(
            "SELECT * FROM aventureiros WHERE nome = ?", (aventureiro.nome,)
        )
        resultado_aventureiros = cursor1.fetchone()
        if resultado_aventureiros is not None:
            raise HTTPException(status_code=400, detail="Aventureiro já existe!")
        cursor1.execute(
            """
            INSERT INTO aventureiros (nome, classe, level) 
            VALUES (?, ?, ?)
        """,
            (aventureiro.nome, aventureiro.classe, aventureiro.level),
        )
    return {"Mensagem": "Aventureiro criado com sucesso!"}


def criar_arma(id_aventureiro: int, arma: Arma):
    """Endpoint para criar uma nova arma.
    - Verifica se a arma já existe no banco de dados.
    -Verifica se o aventureiro já possui 2 armas.
    - Verifica se o dano da arma é compatível com o nível do aventureiro."""
    with conexao() as conn2:
        cursor2 = conn2.cursor()
        cursor2.execute("SELECT * FROM armas WHERE nome_arma = ?", (arma.nome_arma,))
        existencia_arma = cursor2.fetchone()
        if existencia_arma is not None:
            raise HTTPException(status_code=400, detail="A arma já existe!")
        cursor2.execute(
            "SELECT level FROM aventureiros WHERE id = ?", (id_aventureiro,)
        )
        existencia_aventureiro = cursor2.fetchone()
        if existencia_aventureiro is None:
            raise HTTPException(status_code=400, detail="Aventureiro não existe!")
        cursor2.execute(
            """SELECT COUNT(dono_id)
                        FROM armas WHERE dono_id = ?""",
            (id_aventureiro,),
        )
        resultado_aventureiros_arma = cursor2.fetchall()
        if resultado_aventureiros_arma[0][0] >= 2:
            raise HTTPException(
                status_code=400,
                detail="O aventureiro já possui 2 armas, inventario cheio!",
            )
        if arma.dano > existencia_aventureiro[0] * 10:
            raise HTTPException(
                status_code=400,
                detail="A arma é muito poderosa para o nível do aventureiro!",
            )
        cursor2.execute(
            """
            INSERT INTO armas (nome_arma, dano, dono_id)
            VALUES (?, ?, ?)
        """,
            (arma.nome_arma, arma.dano, id_aventureiro),
        )
    return {"Mensagem": "Arma criada com sucesso!"}


def listar_arsenal(id_aventureiro: int):
    """Lista todas as armas de um aventureiro específico.
    -Utilizando o id do aventureiro como parâmetro."""
    with conexao() as conn3:
        cursor3 = conn3.cursor()
        cursor3.execute(
            """
            SELECT * FROM armas WHERE dono_id = ?
        """,
            (id_aventureiro,),
        )
        resultado_arsenal = cursor3.fetchall()
        lista_arsenal = []
        for arsenal in resultado_arsenal:
            id_arma, nome_arma, dano, dono_id = arsenal
            lista_arsenal.append(
                {"id": id_arma, "nome": nome_arma, "dano": dano, "dono_id": dono_id}
            )
    return {"Arsenal": lista_arsenal}
