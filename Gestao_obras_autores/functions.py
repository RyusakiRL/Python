"""Funcões para criar autores e livros, com validação de dados e tratamento de erros."""

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from models import Autor, Livro, Usuario
from schemas import AutorBase, LivroBase, UsuarioCriar
from security import gerar_hash_senha, verificar_senha
from security import criar_token_jwt


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
    livros_autores = (
        db.query(Livro)
        .options(joinedload(Livro.autor))
        .join(Autor)
        .filter(Livro.situacao == True)
        .all()
    )
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


def editar_nomelivro(db: Session, livro_id: int, novo_titulo: str):
    """Edita o nome do livro atraves do id"""
    livro_editar = (
        db.query(Livro).filter(Livro.id == livro_id, Livro.situacao == True).first()
    )

    if not livro_editar:
        raise HTTPException(status_code=404, detail="Livro nao encontrado")

    livro_editar.titulo = novo_titulo
    db.commit()
    db.refresh(livro_editar)
    return {"Mensagem": "Titulo editado com sucesso"}


def quantidade_livro_autor(
    db: Session,
    autor_id: int,
) -> dict:
    """Cria a funcao que lista a quantidade de livros do autor"""
    nome_autor = db.query(Autor.nome).filter(Autor.id == autor_id).scalar()
    if not nome_autor:
        raise HTTPException(status_code=404, detail="Nenhum autor encontrado")
    quantidade = (
        db.query(Livro)
        .filter(Livro.autor_id == autor_id, Livro.situacao == True)
        .count()
    )

    return {"mensagem": f"O autor {nome_autor} tem {quantidade} livros"}


def criar_usuario(db: Session, novo_usuario: UsuarioCriar):
    """Cria um usuario com senha criptografada pelo metodo JWT"""
    if db.query(Usuario).filter(Usuario.email == novo_usuario.email).first():
        raise HTTPException(status_code=400, detail="Email ja existe")
    senha_criptografada = gerar_hash_senha(novo_usuario.senha)
    usuario_novo = Usuario(email=novo_usuario.email, senha=senha_criptografada)

    db.add(usuario_novo)
    db.commit()
    db.refresh(usuario_novo)
    return usuario_novo


def login(db: Session, email: str, senha: str):
    """Logar como usuario"""
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Credenciais incorretas")

    senha_correta = verificar_senha(senha, usuario.senha)

    if not senha_correta:
        raise HTTPException(status_code=400, detail="Credenciais incorretas")
    token = criar_token_jwt({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}
