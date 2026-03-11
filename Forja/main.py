"""Criacao de uma API para cadastro de aventureiros e armas.
A API possui as seguintes funcionalidades:
- Cadastro de aventureiros, com nome, classe e level.
- Cadastro de armas, com nome da arma, dano e id do dono (aventureiro"""

from fastapi import FastAPI
from functions import criar_aventureiro, criar_arma, listar_arsenal
from models import Aventureiro, Arma

app = FastAPI()


@app.post("/aventureiros/")
def criar_aventureiro_endpoint(aventureiro: Aventureiro):
    """Conecta o endpoint de criação de aventureiros com a função criar_aventureiro."""
    return criar_aventureiro(aventureiro)


@app.post("/armas/{id_aventureiro}")
def criar_arma_endpoint(id_aventureiro: int, arma: Arma):
    """Conecta o endpoint de criação de armas com a função criar_arma."""
    return criar_arma(id_aventureiro, arma)


@app.get("/arsenal/{id_aventureiro}")
def listar_arsenal_endpoint(id_aventureiro: int):
    """Conecta o endpoint de listagem de arsenal com a função listar_arsenal."""
    return listar_arsenal(id_aventureiro)
