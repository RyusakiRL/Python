"""Cria os dados e retorna a conexao"""

import sqlite3


def conexao():
    """Cria uma conexão com o banco de dados SQLite e retorna a conexão."""
    return sqlite3.connect("forja.db")


def criar_tabela_guilda():
    """Cria as tabelas 'aventureiros' e 'armas' no banco de dados, caso elas ainda não existam."""
    with conexao() as conn:
        cursor = conn.cursor()
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


criar_tabela_guilda()
