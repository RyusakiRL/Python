"""Cria as validacoes de dados schema"""

from pydantic import BaseModel


class Produtoschem(BaseModel):
    """Cria a validacao de dados schema para Produto"""

    nome: str
    preco: float
    estoque: int
