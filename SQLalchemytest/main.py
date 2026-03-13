"""Retorna os produtos criados no SQLite para aplication FastAPI"""

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from models import ProdutoBase
from funcao import criar_produto
from database import get_db

aplication = FastAPI()


@aplication.post("/produtos/")
def criar_produto_endpoint(produto: ProdutoBase, db: Session = Depends(get_db)):
    """Cria um produto no banco de dados."""
    return criar_produto(produto, db)
