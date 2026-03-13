"""Funcões para criar autores e livros, com validação de dados e tratamento de erros."""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Autor, Livro
from schemas import AutorBase, LivroBase


def criar_autor(db: Session, autor_validacao: AutorBase):
    """Cria um autor no banco de dados, com validação de dados e tratamento de erros."""
    if db.query(Autor).filter(Autor.nome == autor_validacao.nome).first():
        raise HTTPException(status_code=400, detail="Autor já existe.")
    db_autor = Autor(
        nome=autor_validacao.nome,
        nacionalidade=autor_validacao.nacionalidade,
        bio=autor_validacao.bio,
    )
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return {
        "mensagem": "Autor criado com sucesso.",
        "id": db_autor.id,
        "autor": db_autor.nome,
    }


def criar_livro(db: Session, livro_validacao: LivroBase):
    """Cria um livro no banco de dados, com validação de dados e tratamento de erros."""

    if db.query(Livro).filter(Livro.titulo == livro_validacao.titulo).first():
        raise HTTPException(status_code=400, detail="Livro já existe.")
    autor = db.query(Autor).filter(Autor.id == livro_validacao.autor_id).first()

    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado.")

    db_livro = Livro(
        titulo=livro_validacao.titulo,
        autor_id=livro_validacao.autor_id,
        genero=livro_validacao.genero,
    )

    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro


def listar_livros_de_todos_autores(db: Session):
    """Lista os livros de um autor, com validação de dados e tratamento de erros."""
    livros_autores = db.query(Livro).join(Autor).filter(Livro.situacao == True).all()
    if not livros_autores:
        raise HTTPException(status_code=404, detail="Nenhum livro encontrado.")
    return livros_autores


def busca_genero(db: Session, genero: str):
    """Busca livros por gênero, com validação de dados e tratamento de erros."""
    livros_genero = (
        db.query(Livro)
        .filter(Livro.genero.ilike(f"%{genero}%"), Livro.situacao == True)
        .all()
    )
    if not livros_genero:
        raise HTTPException(
            status_code=404, detail="Nenhum livro encontrado para esse gênero."
        )
    return livros_genero


def remover_livro(db: Session, livro_id: int):
    """Remove um livro do banco de dados, com validação de dados e tratamento de erros."""
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    livro.situacao = False
    db.commit()
    return {"mensagem": "Livro removido com sucesso."}
