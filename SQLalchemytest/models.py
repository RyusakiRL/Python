"""Modelos de classe do banco de dados"""

from pydantic import BaseModel


class ProdutoBase(BaseModel):
    """Cria os produtos no SQLite"""

    nome: str
    marca: str
    preco: float
