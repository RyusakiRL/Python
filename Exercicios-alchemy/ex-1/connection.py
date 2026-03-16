"""Retorna a conexao pelo sessionmaker e a engine"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

URL = "sqlite:///produtos.db"

engine = create_engine(URL, echo=False)
Sessionlocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)


def get_db():
    """Retorna a conexao"""
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
