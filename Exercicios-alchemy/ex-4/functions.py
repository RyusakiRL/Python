"""Principais funcoes do sistema"""

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from models import Atleta, Treinador
from schemas import ValidarAtleta, ValidarTreinador
from security import gerar_hash_senha, verificar_senha
from security import criar_token_jwt


def determinar_rank(velocidade: float):
    """determina o rank atraves da velocidade"""
    if velocidade < 10:
        rank = "F"
    elif velocidade >= 10 and velocidade < 15:
        rank = "E"
    elif velocidade >= 15 and velocidade < 20:
        rank = "D"
    elif velocidade >= 20 and velocidade < 25:
        rank = "C"
    elif velocidade >= 25 and velocidade < 30:
        rank = "B"
    elif velocidade >= 30 and velocidade < 35:
        rank = "A"
    elif velocidade >= 35:
        rank = "S"
    else:
        raise HTTPException(status_code=400, detail="Erro na velocidade")
    return rank


def criar_treinador(info_traine: ValidarTreinador, db: Session):
    """Cria o treinador"""
    existencia = (
        db.query(Treinador)
        .filter(Treinador.nome_treinador == info_traine.nome_treinador)
        .first()
    )
    if existencia:
        raise HTTPException(status_code=400, detail="Nome ja existente")
    senha_hash = gerar_hash_senha(info_traine.senha)

    novo_treinador = Treinador(
        nome_treinador=info_traine.nome_treinador, senha=senha_hash
    )
    db.add(novo_treinador)
    db.commit()
    db.refresh(novo_treinador)

    return {"mensagem": "Novo treinador criado com sucesso"}


def login(db: Session, username: str, senha: str):
    """Login do treinador"""
    existencia = (
        db.query(Treinador).filter(Treinador.nome_treinador == username).first()
    )
    if not existencia:
        raise HTTPException(status_code=400, detail="Credencial invalida")

    senha_descrip = verificar_senha(senha, existencia.senha)

    if not senha_descrip:
        raise HTTPException(status_code=400, detail="Credencial invalida")
    token = criar_token_jwt({"sub": existencia.nome_treinador})
    return {"access_token": token, "token_type": "bearer"}


def criar_atleta(db: Session, info_atle: ValidarAtleta, username: str):
    """Cria atleta no banco de dados"""
    id_do_treinador = (
        db.query(Treinador).filter(Treinador.nome_treinador == username).first()
    )
    velocidade = info_atle.status_velocidade
    rank = determinar_rank(velocidade)
    novo_atleta = Atleta(
        nome_atleta=info_atle.nome_atleta,
        rank_atual=rank,
        status_velocidade=info_atle.status_velocidade,
        status_stamina=info_atle.status_stamina,
        id_treinador=id_do_treinador.id,
    )
    db.add(novo_atleta)
    db.commit()
    db.refresh(novo_atleta)
    return {"Mensagem": "Novo atleta adicionado com sucesso a lista"}


def listar_atletas(db: Session, username: str):
    """Lista os atletas de determinado usuario"""
    treinador_nome = (
        db.query(Treinador).filter(Treinador.nome_treinador == username).first()
    )
    if not treinador_nome:
        raise HTTPException(status_code=400, detail="Problema na credencial")
    lista_atletas = (
        db.query(Atleta)
        .options(joinedload(Atleta.trainer))
        .filter(Atleta.id_treinador == treinador_nome.id)
        .all()
    )

    if not lista_atletas:
        raise HTTPException(
            status_code=400, detail="Nao existe nenhum atleta cadastrado"
        )
    return lista_atletas


def atualizar_status(
    db: Session, nome_atleta: str, username: str, nova_velo: float, nova_sta: int
):
    """Atualiza os status do atleta do treinador"""
    treinador_ex = (
        db.query(Treinador).filter(Treinador.nome_treinador == username).first()
    )
    if not treinador_ex:
        raise HTTPException(status_code=400, detail="Erro no login")

    nomenclatura = (
        db.query(Atleta)
        .filter(
            Atleta.nome_atleta == nome_atleta and Atleta.id_treinador == treinador_ex.id
        )
        .first()
    )

    if not nomenclatura:
        raise HTTPException(
            status_code=400, detail="Nao existe nenhum atleta com esse nome"
        )
    new_rank = determinar_rank(nova_velo)
    nomenclatura.status_velocidade = nova_velo
    nomenclatura.status_stamina = nova_sta
    nomenclatura.rank_atual = new_rank

    db.commit()
    db.refresh(nomenclatura)
    return {"mensagem": "status mudados com sucesso"}
