"""Modelos de tabela do banco de dados"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Mercenario(Base):
    """Modelo de banco de dados sqlalchemy que cria a tabela de mercenarios"""

    __tablename__ = "mercenarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    arma = Column(String, nullable=False)
    status = Column(Boolean, default=True)


class Admnistrador(Base):
    """Modelo de banco de dados sqlalchemy que cria a tabela de administrador"""

    __tablename__ = "adms"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    senha = Column(String, nullable=False)
