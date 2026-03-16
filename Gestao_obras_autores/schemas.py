"""Cria os schemas de dados para autores e livros, utilizando Pydantic BaseModel e Literal"""

from typing import Literal
from pydantic import BaseModel


class AutorBase(BaseModel):
    """Cria o schema de dados para autores, com os campos nome, nacionalidade e bio."""

    nome: str
    nacionalidade: str
    bio: str


class LivroBase(BaseModel):
    """Cria o schema de dados para livros, com os campos titulo, autor_id e genero."""

    titulo: str
    autor_id: int
    genero: Literal["Ficção", "Ciência", "Fantasia", "Romance", "Terror", "Aventura"]


class UsuarioCriar(BaseModel):
    """Schema para quando o usuario esta se cadastrando"""

    email: str
    senha: str


class UsuarioResposta(BaseModel):
    """Schema para quando a API devolve os dados do usuario"""

    id: int
    email: str

    model_config = {"from_attributes": True}
