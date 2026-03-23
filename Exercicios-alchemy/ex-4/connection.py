"""Retorna a conexao Session"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


URL_DATABASE = "sqlite:///prancheta.db"

engine = create_engine(URL_DATABASE, echo=False)

SessionLocal = Session(bind=engine, autocommit=False, autoflush=False)


def get_db():
    """Retorna uma conexao segura"""
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
