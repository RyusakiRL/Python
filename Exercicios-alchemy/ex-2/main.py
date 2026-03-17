"""Cria a aplicacao da API"""

from typing import List
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI
from connection import get_db
from security import verificar_token
from schemas import ValidarMercenario
from functions import criar_mercenario, login, listar_mercenario


app = FastAPI()


@app.post("/mercenario/", response_model=ValidarMercenario)
def criar_mercenario_endpoint(
    validacao: ValidarMercenario,
    db: Session = Depends(get_db),
    username_adm: str = Depends(verificar_token),
):
    """Cria os mercenarios no banco de dados se voce for um admnistrador"""
    print(f"O {username_adm} criara novo mercenario")
    return criar_mercenario(validacao=validacao, db=db)


@app.post("/login")
def login_endpoint(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    """Login e retorna o token"""
    username_dig = form_data.username
    senha_dit = form_data.password
    return login(db=db, username=username_dig, senha=senha_dit)


@app.get("/mercenario/{lista}", response_model=List[ValidarMercenario])
def lista_endpoint(
    db: Session = Depends(get_db),
    username_adm: str = Depends(verificar_token),
):
    """Lista os mercenarios da guilda"""
    return listar_mercenario(db)
