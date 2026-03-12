"""Criacao dos modelos de classe"""

from typing import Literal
from pydantic import BaseModel


class Aventureiro(BaseModel):
    """Modelo de dados para representar um aventureiro, com nome, classe e level."""

    nome: str
    classe: Literal["Guerreiro", "Mago", "Arqueiro"]
    level: int


class Arma(BaseModel):
    """Modelo de daddo de uma arma, com nome da arma, dano e id do dono (aventureiro)."""

    nome_arma: str
    dano: int


class Contrato(BaseModel):
    """Modelo de dados para representar um contrato."""

    nome_monstro: str
    recompensa: int
    rank_minimo: int


class PerfilAventureiro(BaseModel):
    """Modelo de dados para representar o perfil de um aventureiro."""

    nome: str
    classe: Literal["Guerreiro", "Mago", "Arqueiro"]
