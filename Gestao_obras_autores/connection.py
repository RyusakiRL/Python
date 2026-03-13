"""Retorna a conexao com o banco de dados.
-utilizando SQLAlchemy ORM, alem da engine e da sessionlocal."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "sqlite:///livros_autores.db"

engine = create_engine(URL_DATABASE, echo=False)
Sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    """Responsavel por criar a conexao com o banco de dados
    -utilizando SQLAlchemy ORM, e fechar a conexao apos o uso."""
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
