"""Cria a aplicação FastAPI."""

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from connection import get_db
from functions import (
    busca_genero,
    criar_autor,
    criar_livro,
    listar_livros_de_todos_autores,
    remover_livro,
    editar_nomelivro,
    quantidade_livro_autor,
)
from schemas import AutorBase, LivroBase

app = FastAPI()


@app.post("/autores/")
def criar_autor_endpoint(autor: AutorBase, db: Session = Depends(get_db)):
    """Endpoint para criar um autor, utilizando a função criar_autor."""
    return criar_autor(db, autor)


@app.post("/livros/")
def criar_livro_endpoint(livro: LivroBase, db: Session = Depends(get_db)):
    """Endpoint para criar um livro, utilizando a função criar_livro."""
    return criar_livro(db, livro)


@app.get("/livros/autores")
def listar_livros_endpoint(db: Session = Depends(get_db)):
    """Endpoint para listar todos os livros, utilizando a função listar_livros_de_todos_autores."""
    return listar_livros_de_todos_autores(db)


@app.get("/livros/genero/{genero}")
def busca_genero_endpoint(genero: str, db: Session = Depends(get_db)):
    """Endpoint para buscar livros por gênero, utilizando a função busca_genero."""
    return busca_genero(db, genero)


@app.delete("/livros/{livro_id}")
def excluir_livro_endpoint(livro_id: int, db: Session = Depends(get_db)):
    """Endpoint para excluir um livro, utilizando a função excluir_livro."""
    return remover_livro(db, livro_id)


@app.put("/livros/editar/{livro_id}")
def editar_livro_endpoint(
    id_livro: int, novo_titulo: str, db: Session = Depends(get_db)
):
    """Edita o titulo de um livro a partir de seu id"""
    return editar_nomelivro(db, id_livro, novo_titulo)


@app.get("/autor/{autor_id}/livros")
def listar_livros_autor_endpoint(autor_id: int, db: Session = Depends(get_db)):
    """Lista a quantidade de livros escritos por determinado autor"""

    return quantidade_livro_autor(db, autor_id)
