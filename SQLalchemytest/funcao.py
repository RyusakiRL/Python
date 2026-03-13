"""funcoes do documento principal, onde tem as funcoes para criar os produtos no banco de dados"""

from sqlalchemy.orm import Session
from database import Produto
from models import ProdutoBase


def criar_produto(produto: ProdutoBase, db: Session):
    """Cria um produto no banco de dados."""
    novo_produto = Produto(
        nome=produto.nome,
        marca=produto.marca,
        preco=produto.preco,
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return {
        "Mensagem": "Produto criado com sucesso!",
        "nome": novo_produto.nome,
        "id": novo_produto.id,
    }
