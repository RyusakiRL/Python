"""Cria os modelos de dados para autores e livros, utilizando SQLAlchemy ORM."""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from connection import engine

Base = declarative_base()


class Autor(Base):
    """Criacao da tabela de autores, com os campos id, nome, nacionalidade e bio."""

    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False, unique=True)
    nacionalidade = Column(String, nullable=False)
    bio = Column(String, nullable=False)
    livros = relationship("Livro", back_populates="autor")


class Livro(Base):
    """Criacao da tabela de livros, com os campos id, titulo, autor_id e situacao."""

    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True, nullable=False, unique=True)
    genero = Column(String, nullable=False)
    autor_id = Column(Integer, ForeignKey("autores.id"), nullable=False)
    situacao = Column(Boolean, default=True)
    ano_publi = Column(String, nullable=False)
    autor = relationship("Autor", back_populates="livros")


Base.metadata.create_all(bind=engine)
