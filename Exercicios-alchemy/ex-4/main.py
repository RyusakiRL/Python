"""Liga o sistema a API"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from connection import get_db
from functions import (
    atualizar_status,
    criar_atleta,
    criar_treinador,
    listar_atletas,
    login,
)
from schemas import ValidarAtleta, ValidarTreinador, ModeloRespostaAtleta
from security import verificar_token


app = FastAPI()


@app.post("/treinador")
def criar_treinador_endpoint(
    treinador: ValidarTreinador, db: Session = Depends(get_db)
):
    """Cria o treinador que ira atualizar os cadastros de seus atletas"""
    return criar_treinador(db=db, info_traine=treinador)


@app.post("/login")
def rota_login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    """Rota de login como treinador"""
    nome = form_data.username
    senha = form_data.password
    return login(db=db, username=nome, senha=senha)


@app.post("/treinador/atleta")
def criar_atleta_endpoint(
    atleta: ValidarAtleta,
    db: Session = Depends(get_db),
    username_trein: Session = Depends(verificar_token),
):
    """Cria atleta para determinado treinador"""
    return criar_atleta(db=db, info_atle=atleta, username=username_trein)


@app.get("/treinador/lista", response_model=List[ModeloRespostaAtleta])
def listar_atleta_endpoint(
    db: Session = Depends(get_db), username_trein: Session = Depends(verificar_token)
):
    """Lista os atletas de determinado treinador"""
    return listar_atletas(db=db, username=username_trein)


@app.put("/treinador/atleta/atualizar")
def atualizar_atleta_endpoint(
    nome_atleta: str,
    nova_velocidade_km_h: float,
    nova_stamina: int,
    db: Session = Depends(get_db),
    username_trein: Session = Depends(verificar_token),
):
    """Atualiza os status dos atletas"""
    return atualizar_status(
        db=db,
        nome_atleta=nome_atleta,
        username=username_trein,
        nova_velo=nova_velocidade_km_h,
        nova_sta=nova_stamina,
    )
