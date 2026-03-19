"""Retorna a conexao get_db"""

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

URL_DATABASE = "sqlite:///presets.db"

engine = create_engine(URL_DATABASE, echo=False)

SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Funcao que retorna a conexao da Sessao"""
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
