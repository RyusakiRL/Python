"""Conexao com o banco de dados."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


URL_BANCO = "sqlite:///sandbox.db"
engine = create_engine(URL_BANCO, echo=False)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Gerar uma sessão de banco de dados para cada solicitação."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
