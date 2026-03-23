"""Moldes de criacao de tabela SQL"""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, String, ForeignKey, Column, Float

Base = declarative_base()


class Treinador(Base):
    """Cria a tabela SQL de treinador com seguranca JWT"""

    __tablename__ = "treinador"
    id = Column(Integer, primary_key=True, index=True)
    nome_treinador = Column(String, nullable=False, unique=True, index=True)
    senha = Column(String, nullable=False)
    corredores = relationship("Atleta", back_populates="trainer")


class Atleta(Base):
    """Cria a tabela SQL dos atletas"""

    __tablename__ = "atleta"
    id = Column(Integer, primary_key=True, index=True)
    nome_atleta = Column(String, nullable=False, index=True)
    rank_atual = Column(String, nullable=False)
    status_velocidade = Column(Float, nullable=False)
    status_stamina = Column(Integer, nullable=False)
    id_treinador = Column(Integer, ForeignKey("treinador.id"), nullable=False)
    trainer = relationship("Treinador", back_populates="corredores")
