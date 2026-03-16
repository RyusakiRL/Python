"""Cria o SQL da tabela"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Produto(Base):
    """Cria a tabela de produtos"""

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True, unique=True)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
