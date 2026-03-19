"""Moldes de schemas para validacao de dados"""

from pydantic import BaseModel, ConfigDict


class PresetsValidacao(BaseModel):
    """Validacao dos dados do presets"""

    nome_musica: str
    software_usado: str
    nivel_ganho: float
    distorcao: bool
    model_config = ConfigDict(from_attributes=True)


class ValidarProdutor(BaseModel):
    """Validacao dos dados para criar um produtor"""

    username: str
    senha: str
