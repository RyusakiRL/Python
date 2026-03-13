"""Teste para gerar um banco de dados usando SQLAlchemy."""

from sqlalchemy import Column, create_engine, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. O Motor: Criamos a conexão.
# A mágica do Sênior: o "echo=True" faz o terminal imprimir todo o SQL que o SQLAlchemy
URL_BANCO = "sqlite:///sandbox.db"
engine = create_engine(URL_BANCO, echo=True)

# 2. A Fábrica de Sessões: É ela que vai gerar as sessões para inserirmos os dados depois.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. O Molde Base: Todas as nossas tabelas vão nascer a partir dessa variável.
Base = declarative_base()


class Produto(Base):
    """Cria os produtos no SQLite"""

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    marca = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, default=0)


Base.metadata.create_all(bind=engine)


def get_db():
    """Gerar uma sessão de banco de dados para cada solicitação."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
