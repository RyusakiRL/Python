"""Cria os dados e retorna a conexao"""

import sqlite3


def conexao():
    """Cria uma conexão com o banco de dados 'forja.db' e a retorna.
    - A conexão é fechada automaticamente após o uso, graças ao gerenciador de contexto 'yield'.
    """
    conn = sqlite3.connect("forja.db")
    try:
        yield conn
    finally:
        conn.close()


def criar_tabela_guilda():
    """Cria as tabelas 'aventureiros' e 'armas' no banco de dados, caso elas ainda não existam."""
    with sqlite3.connect("forja.db") as connect:
        cursor = connect.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS aventureiros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                classe TEXT NOT NULL,
                level integer NOT NULL
            )"""
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS armas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_arma TEXT NOT NULL UNIQUE,
                dano INTEGER NOT NULL,
                dono_id INTEGER NOT NULL,
                FOREIGN KEY (dono_id) REFERENCES aventureiros(id)
            )"""
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contratos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_monstro TEXT NOT NULL,
                recompensa INTEGER NOT NULL,
                rank_minimo INTEGER NOT NULL,
                id_aventureiro INTEGER,
                FOREIGN KEY (id_aventureiro) REFERENCES aventureiros(id)
            )"""
        )


criar_tabela_guilda()
