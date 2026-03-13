"""Cria as tabelas do SQLite usando SQLAlchemy."""

from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()


class ProdutoSQL(Base):
    """Cria os produtos no SQLite"""

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    marca = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)
