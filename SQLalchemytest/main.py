"""Retorna os produtos criados no SQLite para aplication FastAPI"""

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from schemas import Produtovalidacao
from funcao import (
    adicionar_estoque,
    criar_produto,
    listar_produtos,
    procurar_produto,
    produtos_black_friday,
    remover_produto,
    vender_produto,
)
from database import get_db

aplication = FastAPI()


@aplication.post("/produtos/")
def criar_produto_endpoint(produto: Produtovalidacao, db: Session = Depends(get_db)):
    """Cria um produto no banco de dados."""
    return criar_produto(produto, db)


@aplication.put("/produtos/{produto_id}/adicionar-estoque/")
def adicionar_estoque_endpoint(
    produto_id: int, quantidade: int, db: Session = Depends(get_db)
):
    """Adiciona uma quantidade ao estoque de um produto."""
    return adicionar_estoque(produto_id, quantidade, db)


@aplication.get("/produtos/estoque/")
def listar_produtos_endpoint(db: Session = Depends(get_db)):
    """Lista todos os produtos do banco de dados."""
    return listar_produtos(db)


@aplication.get("/produtos/black-friday/{preco_maximo}/")
def produtos_black_friday_endpoint(preco_maximo: float, db: Session = Depends(get_db)):
    """Lista os produtos com preço abaixo do valor especificado."""
    return produtos_black_friday(preco_maximo, db)


@aplication.get("/produtos/busca/{termo_pesquisa}")
def procurar_produto_endpoint(termo_pesquisa: str, db: Session = Depends(get_db)):
    """Procura um produto pelo nome."""
    return procurar_produto(termo_pesquisa, db)


@aplication.put("/produtos/{produto_id}/vender/")
def vender_produto_endpoint(
    produto_id: int, quantidade: int, db: Session = Depends(get_db)
):
    """Vende uma quantidade de um produto, reduzindo o estoque."""
    return vender_produto(produto_id, quantidade, db)


@aplication.delete("/produtos/{produto_id}/remover/")
def remover_produto_endpoint(produto_id: int, db: Session = Depends(get_db)):
    """Remove um produto do banco de dados."""
    return remover_produto(produto_id, db)
