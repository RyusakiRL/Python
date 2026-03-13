"""funcoes do documento principal, onde tem as funcoes para criar os produtos no banco de dados"""

from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import ProdutoSQL
from schemas import Produtovalidacao


def criar_produto(produto: Produtovalidacao, db: Session):
    """Cria um produto no banco de dados."""
    existencia = db.query(ProdutoSQL).filter(ProdutoSQL.nome == produto.nome).first()
    if existencia:
        raise HTTPException(status_code=400, detail="Produto já existe.")
    novo_produto = ProdutoSQL(
        nome=produto.nome,
        marca=produto.marca,
        preco=produto.preco,
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return {
        "Mensagem": "Produto criado com sucesso!",
        "nome": novo_produto.nome,
        "id": novo_produto.id,
    }


def listar_produtos(db: Session):
    """Lista todos os produtos do banco de dados."""
    estoque = db.query(ProdutoSQL).filter(ProdutoSQL.ativo is True).all()
    return estoque


def procurar_produto(nome_produto: str, db: Session):
    """Procura um produto pelo nome."""
    produto = (
        db.query(ProdutoSQL)
        .filter(ProdutoSQL.nome.ilike(f"%{nome_produto}%"), ProdutoSQL.ativo is True)
        .first()
    )
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return produto


def produtos_black_friday(produto_preco: float, db: Session):
    """Lista os produtos com preço abaixo do valor especificado."""
    produtos = (
        db.query(ProdutoSQL)
        .filter(ProdutoSQL.preco <= produto_preco, ProdutoSQL.ativo is True)
        .all()
    )
    if not produtos:
        raise HTTPException(
            status_code=404,
            detail="Nenhum produto encontrado com preço abaixo do valor especificado.",
        )
    return produtos


def adicionar_estoque(produto_id: int, quantidade: int, db: Session):
    """Adiciona uma quantidade ao estoque de um produto."""
    produto = (
        db.query(ProdutoSQL)
        .filter(ProdutoSQL.id == produto_id, ProdutoSQL.ativo is True)
        .first()
    )
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    produto.quantidade += quantidade
    db.commit()
    db.refresh(produto)

    return {
        "Mensagem": f"Estoque atualizado. Quantidade atual: {produto.quantidade}",
        "nome": produto.nome,
        "quantidade": produto.quantidade,
    }


def vender_produto(produto_id: int, quantidade: int, db: Session):
    """Vende uma quantidade de um produto, reduzindo o estoque."""
    produto = db.query(ProdutoSQL).filter(ProdutoSQL.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    if produto.quantidade < quantidade:
        raise HTTPException(
            status_code=400,
            detail=f"Estoque insuficiente. Quantidade disponível: {produto.quantidade}",
        )
    valor_total = produto.preco * quantidade
    produto.quantidade -= quantidade
    db.commit()
    db.refresh(produto)

    return {
        "Mensagem": f"Venda realizada. Valor total: R${valor_total:.2f}",
        "nome": produto.nome,
        "quantidade restante": produto.quantidade,
    }


def remover_produto(produto_id: int, db: Session):
    """Remove uma quantidade do estoque de um produto."""
    produto = db.query(ProdutoSQL).filter(ProdutoSQL.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    produto.ativo = False
    db.commit()
    db.refresh(produto)

    return {"mensagem": f"Produto '{produto.nome}' removido com sucesso."}
