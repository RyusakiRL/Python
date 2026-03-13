"""Modelos de classe do banco de dados"""

from pydantic import BaseModel


class Produtovalidacao(BaseModel):
    """Cria os produtos no SQLite"""

    nome: str
    marca: str
    preco: float
