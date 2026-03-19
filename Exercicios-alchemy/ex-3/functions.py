"""Principais funcoes do sistema"""

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from models import Produtor, Preset
from schemas import PresetsValidacao, ValidarProdutor
from security import gerar_hash_senha, verificar_senha
from security import criar_token_jwt


def criar_produtor(validp: ValidarProdutor, db: Session):
    """Cria um produtor"""
    existencia = db.query(Produtor).filter(Produtor.username == validp.username).first()
    if existencia:
        raise HTTPException(status_code=400, detail="Nome ja existe")

    senha_criptografada = gerar_hash_senha(validp.senha)

    novo_produtor = Produtor(username=validp.username, senha=senha_criptografada)
    db.add(novo_produtor)
    db.commit()
    db.refresh(novo_produtor)
    return {"mensagem": "Produtor criado com sucesso"}


def login(db: Session, username: str, senha: str):
    """cria o login entre o produtor e a conta"""
    existencia = db.query(Produtor).filter(Produtor.username == username).first()
    if not existencia:
        raise HTTPException(status_code=400, detail="Credenciais invalidas")

    senha_verdadeira = verificar_senha(senha, existencia.senha)

    if not senha_verdadeira:
        raise HTTPException(status_code=400, detail="Credenciais invalidas")
    token = criar_token_jwt({"sub": existencia.username})
    return {"access_token": token, "token_type": "bearer"}


def criar_preset(db: Session, validarpre: PresetsValidacao, username: str):
    """Cria os presets da musicas para o usuario salvo"""
    existencia_preset = (
        db.query(Preset).filter(Preset.nome_musica == validarpre.nome_musica).first()
    )
    if existencia_preset:
        raise HTTPException(status_code=400, detail="Nome ja existe insira outro nome")
    id_produtor = db.query(Produtor).filter(Produtor.username == username).first()
    if not id_produtor:
        raise HTTPException(status_code=400, detail="nao existe produtor")
    novo_preset = Preset(
        nome_musica=validarpre.nome_musica,
        software_usado=validarpre.software_usado,
        nivel_ganho=validarpre.nivel_ganho,
        distorcao=validarpre.distorcao,
        user_id=id_produtor.id,
    )

    db.add(novo_preset)
    db.commit()
    db.refresh(novo_preset)

    return {"mensagem": "Novo preset adicionado"}


def listar_presets(db: Session, user: str):
    """Lista os presets do usuario"""
    produtor_nome = db.query(Produtor).filter(Produtor.username == user).first()
    if not produtor_nome:
        raise HTTPException(status_code=400, detail="Problema na credencial")
    lista = (
        db.query(Preset)
        .options(joinedload(Preset.user))
        .join(Produtor)
        .filter(Produtor.id == produtor_nome.id)
        .all()
    )

    if not lista:
        raise HTTPException(
            status_code=400, detail="Nenhum preset existente do Produtor"
        )
    return lista
