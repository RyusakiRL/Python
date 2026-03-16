"""Funcoes do sistema main"""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Produto
from schema import Produtoschem


def criar_produto(db: Session, produto_validacao: Produtoschem):
    """Cria um produto novo"""
    if db.query(Produto).filter(Produto.nome == produto_validacao.nome).first():
        raise HTTPException(status_code=400, detail="Nome de produto ja existe")

    new_produto = Produto(
        nome=produto_validacao.nome,
        preco=produto_validacao.preco,
        estoque=produto_validacao.estoque,
    )
    db.add(new_produto)
    db.commit()
    db.refresh(new_produto)
    return {"mensagem": "Produto criado com sucesso"}


def listar_produtos(db: Session):
    """lista todos os produtos"""
    lista_produtos = db.query(Produto).all()
    if not lista_produtos:
        raise HTTPException(
            status_code=400, detail="Nao existe nenhum produto no banco de dados"
        )
    return lista_produtos
