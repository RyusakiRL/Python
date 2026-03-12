"""Funcoes do sistema de cadastro de aventureiros e armas."""

import sqlite3
from fastapi import HTTPException
from models import Aventureiro, Arma, Contrato


def criar_aventureiro(aventureiro: Aventureiro, conn: sqlite3.Connection):
    """Endpoint para criar um novo aventureiro.
    - Verifica se o aventureiro já existe no banco de dados."""

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aventureiros WHERE nome = ?", (aventureiro.nome,))
    resultado_aventureiros = cursor.fetchone()
    if resultado_aventureiros is not None:
        raise HTTPException(status_code=400, detail="Aventureiro já existe!")
    cursor.execute(
        """
        INSERT INTO aventureiros (nome, classe, level) 
         VALUES (?, ?, ?)
        """,
        (aventureiro.nome, aventureiro.classe, aventureiro.level),
    )
    conn.commit()
    return {"Mensagem": "Aventureiro criado com sucesso!"}


def criar_arma(id_aventureiro: int, arma: Arma, conn2: sqlite3.Connection):
    """Endpoint para criar uma nova arma.
    - Verifica se a arma já existe no banco de dados.
    -Verifica se o aventureiro já possui 2 armas.
    - Verifica se o dano da arma é compatível com o nível do aventureiro."""

    cursor2 = conn2.cursor()
    cursor2.execute("SELECT * FROM armas WHERE nome_arma = ?", (arma.nome_arma,))
    existencia_arma = cursor2.fetchone()
    if existencia_arma is not None:
        raise HTTPException(status_code=400, detail="A arma já existe!")
    cursor2.execute("SELECT level FROM aventureiros WHERE id = ?", (id_aventureiro,))
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
    conn2.commit()
    return {"Mensagem": "Arma criada com sucesso!"}


def criar_contrato(contrato: Contrato, conn4: sqlite3.Connection):
    """Endpoint para criar um novo contrato.
    - Verifica se o contrato já existe no banco de dados.
    - Verifica se o aventureiro existe no banco de dados.
    - Verifica se o nível do aventureiro é compatível com o rank mínimo do contrato."""

    cursor4 = conn4.cursor()
    cursor4.execute(
        "SELECT * FROM contratos WHERE nome_monstro = ?", (contrato.nome_monstro,)
    )
    existencia_contrato = cursor4.fetchone()
    if existencia_contrato is not None:
        raise HTTPException(status_code=400, detail="Contrato já existe!")
    cursor4.execute(
        """
        INSERT INTO contratos (nome_monstro, recompensa, rank_minimo, id_aventureiro)
        VALUES (?, ?, ?, ?)
    """,
        (
            contrato.nome_monstro,
            contrato.recompensa,
            contrato.rank_minimo,
            None,
        ),
    )
    conn4.commit()
    return {"Mensagem": "Contrato criado com sucesso!"}


def listar_arsenal(id_aventureiro: int, conn3: sqlite3.Connection):
    """Lista todas as armas de um aventureiro específico.
    -Utilizando o id do aventureiro como parâmetro."""

    conn3.row_factory = sqlite3.Row
    cursor3 = conn3.cursor()
    cursor3.execute(""" SELECT * FROM armas WHERE dono_id = ?""", (id_aventureiro,))
    resultado_arsenal = cursor3.fetchall()
    if not resultado_arsenal:
        raise HTTPException(status_code=400, detail="Aventureiro não possui armas!")
    return [dict(linha) for linha in resultado_arsenal]


def listar_contratos(conn5: sqlite3.Connection):
    """Lista todos os contratos de um aventureiro específico.
    -Utilizando o id do aventureiro como parâmetro."""

    conn5.row_factory = sqlite3.Row
    cursor5 = conn5.cursor()
    cursor5.execute(""" SELECT * FROM contratos""")
    resultado_contratos = cursor5.fetchall()
    if not resultado_contratos:
        raise HTTPException(
            status_code=400, detail="Não existem contratos cadastrados!"
        )
    return [dict(linha) for linha in resultado_contratos]


def listar_aventureiros(conn7: sqlite3.Connection):
    """Lista todos os aventureiros cadastrados no banco de dados."""

    conn7.row_factory = sqlite3.Row
    cursor7 = conn7.cursor()
    cursor7.execute(""" SELECT * FROM aventureiros""")
    resultado_aventureiros = cursor7.fetchall()
    if not resultado_aventureiros:
        raise HTTPException(
            status_code=400, detail="Não existem aventureiros cadastrados!"
        )
    return [dict(linha) for linha in resultado_aventureiros]


def aceitar_contrato(id_contrato: int, id_aventureiro: int, conn6: sqlite3.Connection):
    """Permite que um aventureiro aceite um contrato específico.
    - Verifica se o contrato existe no banco de dados.
    - Verifica se o contrato já foi aceito por outro aventureiro.
    - Verifica se o nível do aventureiro é compatível com o rank mínimo do contrato."""

    cursor6 = conn6.cursor()
    cursor6.execute("SELECT * FROM contratos WHERE id = ?", (id_contrato,))
    existencia_contrato = cursor6.fetchone()
    if existencia_contrato is None:
        raise HTTPException(status_code=400, detail="Contrato não existe!")
    if existencia_contrato[4] is not None:
        raise HTTPException(status_code=400, detail="Contrato já foi aceito!")
    cursor6.execute("SELECT level FROM aventureiros WHERE id = ?", (id_aventureiro,))
    existencia_aventureiro = cursor6.fetchone()
    if existencia_aventureiro is None:
        raise HTTPException(status_code=400, detail="Aventureiro não existe!")
    if existencia_contrato[3] > existencia_aventureiro[0]:
        raise HTTPException(
            status_code=400,
            detail="O nível do aventureiro é muito baixo para aceitar esse contrato!",
        )
    cursor6.execute(
        """
        UPDATE contratos
        SET id_aventureiro = ?
        WHERE id = ?
    """,
        (id_aventureiro, id_contrato),
    )
    conn6.commit()
    return {"Mensagem": "Contrato aceito com sucesso!"}
