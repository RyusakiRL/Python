"""Valida os mercenarios"""

from pydantic import BaseModel, ConfigDict


class ValidarMercenario(BaseModel):
    """Classe que valida os mercenarios para ir para o banco de dados"""

    nome: str
    arma: str
    model_config = ConfigDict(from_attributes=True)


class ValidarAdm(BaseModel):
    """Classe que valida os valores de adm para ir ao banco de dados"""

    username: str
    senha: str
