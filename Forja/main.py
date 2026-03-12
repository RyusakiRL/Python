"""Criacao de uma API para cadastro de aventureiros e armas.
A API possui as seguintes funcionalidades:
- Cadastro de aventureiros, com nome, classe e level.
- Cadastro de armas, com nome da arma, dano e id do dono (aventureiro"""

import sqlite3
from fastapi import FastAPI, Depends
from database import conexao
from functions import (
    criar_aventureiro,
    criar_arma,
    listar_arsenal,
    criar_contrato,
    listar_aventureiros,
    listar_contratos,
    aceitar_contrato,
)
from models import Aventureiro, Arma, Contrato, PerfilAventureiro

app = FastAPI()


@app.post("/aventureiros/")
def criar_aventureiro_endpoint(
    aventureiro: Aventureiro, banco_de_dados: sqlite3.Connection = Depends(conexao)
):
    """Conecta o endpoint de criação de aventureiros com a função criar_aventureiro."""
    return criar_aventureiro(aventureiro, banco_de_dados)


@app.post("/armas/{id_aventureiro}")
def criar_arma_endpoint(
    id_aventureiro: int,
    arma: Arma,
    banco_de_dados: sqlite3.Connection = Depends(conexao),
):
    """Conecta o endpoint de criação de armas com a função criar_arma."""
    return criar_arma(id_aventureiro, arma, banco_de_dados)


@app.post("/contratos/")
def criar_contrato_endpoint(
    contrato: Contrato,
    banco_de_dados: sqlite3.Connection = Depends(conexao),
):
    """Conecta o endpoint de criação de contratos com a função criar_contrato."""
    return criar_contrato(contrato, banco_de_dados)


@app.get("/arsenal/{id_aventureiro}", response_model=list[Arma])
def listar_arsenal_endpoint(
    id_aventureiro: int, banco_de_dados: sqlite3.Connection = Depends(conexao)
):
    """Conecta o endpoint de listagem de arsenal com a função listar_arsenal."""
    return listar_arsenal(id_aventureiro, banco_de_dados)


@app.get("/contratos/lista", response_model=list[Contrato])
def listar_contratos_endpoint(banco_de_dados: sqlite3.Connection = Depends(conexao)):
    """Conecta o endpoint de listagem de contratos com a função listar_contratos."""

    return listar_contratos(banco_de_dados)


@app.get(
    "/contratos/lista/aventureiro/{id_aventureiro}",
    response_model=list[PerfilAventureiro],
)
def listar_aventureiros_endpoint(banco_de_dados: sqlite3.Connection = Depends(conexao)):
    """Conecta o endpoint de listagem de aventureiros com a função listar_aventureiros."""
    return listar_aventureiros(banco_de_dados)


@app.put("/contratos/assinar/{id_contrato}/{id_aventureiro}")
def assinar_contrato_endpoint(
    id_contrato: int,
    id_aventureiro: int,
    banco_de_dados: sqlite3.Connection = Depends(conexao),
):
    """Conecta o endpoint de assinatura de contrato com a função assinar_contrato."""
    return aceitar_contrato(id_contrato, id_aventureiro, banco_de_dados)
