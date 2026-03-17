"""Principais funcoes do sistema"""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Mercenario, Admnistrador
from schemas import ValidarMercenario
from security import criar_token_jwt, verificar_senha


def login(username: str, senha: str, db: Session):
    """Logar como usuario"""
    usuario = db.query(Admnistrador).filter(Admnistrador.username == username).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Credenciais incorretas")

    senha_correta = verificar_senha(senha, usuario.senha)

    if not senha_correta:
        raise HTTPException(status_code=400, detail="Credenciais incorretas")

    token = criar_token_jwt({"sub": usuario.username})
    return {"access_token": token, "token_type": "bearer"}


def criar_mercenario(validacao: ValidarMercenario, db: Session):
    """Funcao de criar mercenario"""
    existencia = db.query(Mercenario).filter(Mercenario.nome == validacao.nome).first()
    if existencia:
        raise HTTPException(status_code=400, detail="Mercenario ja existe")

    novo_mercenario = Mercenario(nome=validacao.nome, arma=validacao.arma)

    db.add(novo_mercenario)
    db.commit()
    db.refresh(novo_mercenario)
    return novo_mercenario


def listar_mercenario(db: Session):
    """Funcao com o objetivo de listar todos os mercenarios da guilda"""
    listar_todos = db.query(Mercenario).all()

    return listar_todos
