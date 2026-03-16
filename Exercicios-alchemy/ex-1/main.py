"""Faz a conexao dos arquivos com a API"""

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from connection import get_db
from schema import Produtoschem
from functions import criar_produto, listar_produtos

app = FastAPI()


@app.post("/produto/criar")
def criar_produto_endpoint(
    produto_validacao: Produtoschem, db: Session = Depends(get_db)
):
    """Conecta a criacao de produto a API"""
    return criar_produto(db, produto_validacao)


@app.get("/produto/listar", response_model=list[Produtoschem])
def listar_produtos_endpoint(db: Session = Depends(get_db)):
    """Lista todos os produtos da loja"""
    return listar_produtos(db)
