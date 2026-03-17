"""Cria os admnistradores diretamente no terminal, sem conectar com API"""

from models import Admnistrador
from schemas import ValidarAdm
from security import gerar_hash_senha
from connection import get_db

NOME = input("Insira o nome para criar um novo administrador: ")
SENHA = str(input("Insira a senha para criar um novo admnistrador:  "))
novo_adm = ValidarAdm(username=NOME, senha=SENHA)
db = next(get_db())


def criar_adm(new_adm: ValidarAdm, db_session):
    """Cria os admnistradores e valida alguns possiveis erros"""

    if (
        db_session.query(Admnistrador)
        .filter(Admnistrador.username == new_adm.username)
        .first()
    ):
        print("Ja existe esse admnistrador")

    else:
        senha_hasheada = gerar_hash_senha(new_adm.senha)
        novo_admnistrador = Admnistrador(
            username=new_adm.username, senha=senha_hasheada
        )
        db_session.add(novo_admnistrador)
        db_session.commit()
        db_session.close()
        print("Administrador registrado com sucesso")


criar_adm(new_adm=novo_adm, db_session=db)
