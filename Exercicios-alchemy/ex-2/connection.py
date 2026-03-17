"""Retorna a conexao da sessao atraves do yield e finally"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

URL_DATA = "sqlite:///gestao_mercenarios.db"
engine = create_engine(URL_DATA, echo=False)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    """Retorna a conexao e fecha para nao sobrecarregar o sistema"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
