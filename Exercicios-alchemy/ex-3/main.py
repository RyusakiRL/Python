"""Cria a aplicacao para conectar a API"""

from typing import List
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI
from connection import get_db
from schemas import PresetsValidacao, ValidarProdutor
from security import verificar_token
from functions import criar_produtor, criar_preset, login, listar_presets

app = FastAPI()


@app.post("/login")
def login_endpoint(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    """Loga como produtor do sistema"""
    username_digitado = form_data.username
    senha_digitada = form_data.password
    return login(db=db, username=username_digitado, senha=senha_digitada)


@app.post("/produtor/")
def criar_produtor_endpoint(validp: ValidarProdutor, db: Session = Depends(get_db)):
    """cria os produtores"""

    return criar_produtor(validp=validp, db=db)


@app.post("/produtor/preset")
def criar_preset_endpoint(
    validarpre: PresetsValidacao,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token),
):
    """Cria os presets do usuario"""
    return criar_preset(db=db, validarpre=validarpre, username=usuario)


@app.get("/produtor/lista", response_model=List[PresetsValidacao])
def listar_preset_endpoint(
    db: Session = Depends(get_db), produtor: str = Depends(verificar_token)
):
    """Conecta a lista de presets de determinado Produtor"""

    return listar_presets(db=db, user=produtor)
