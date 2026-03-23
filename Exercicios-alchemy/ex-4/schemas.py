"""Validacao de valores"""

from pydantic import BaseModel, ConfigDict


class ValidarTreinador(BaseModel):
    """Valida os valores de treinador"""

    nome_treinador: str
    senha: str


class ValidarAtleta(BaseModel):
    """Validar os valores atraves de classe para os atletas"""

    nome_atleta: str
    status_velocidade: float
    status_stamina: int


class ModeloRespostaAtleta(BaseModel):
    """Apenas para mostrar os valores determinados de tal atleta"""

    nome_atleta: str
    rank_atual: str
    status_velocidade: float
    status_stamina: int
    model_config = ConfigDict(from_attributes=True)
