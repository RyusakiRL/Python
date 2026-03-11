from pydantic import BaseModel


class Aventureiro(BaseModel):
    """Modelo de dados para representar um aventureiro, com nome, classe e level."""

    nome: str
    classe: str
    level: int


class Arma(BaseModel):
    """Modelo de daddo de uma arma, com nome da arma, dano e id do dono (aventureiro)."""

    nome_arma: str
    dano: int
