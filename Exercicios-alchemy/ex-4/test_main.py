"""Pytest"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from connection import get_db
from models import Base

# ====================================================================
# 1. INFRAESTRUTURA (O Boilerplate que você copia e cola)
# ====================================================================

# Criamos um banco de dados temporário só para os testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_banco_temporario.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Deleta a tabela antiga e depois cria as tabelas do zero nesse banco fantasma
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


# Função que "engana" o FastAPI para ele usar o banco falso ao invés do oficial
def override_get_db():
    """Faz o fastapi usar o banco de dados falso"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# Trocando o banco real pelo banco de teste
app.dependency_overrides[get_db] = override_get_db

# O nosso "Robô" que vai clicar no Swagger por nós
client = TestClient(app)


# ====================================================================
# 2. OS TESTES (A sua lógica de validação)
# ====================================================================


def test_criar_treinador_com_sucesso():
    """Simula a criação de um treinador no Swagger"""

    # O robô manda o POST com o JSON
    response = client.post(
        "/treinador", json={"nome_treinador": "Ryusaki", "senha": "123"}
    )

    # Verificamos (assert) se a Catraca devolveu o Status 200 (OK)
    assert response.status_code == 200

    # Verificamos se a mensagem no corpo da resposta é exatamente a que programamos
    assert response.json() == {"mensagem": "Novo treinador criado com sucesso"}


def test_barrar_intruso_sem_token():
    """Simula um hacker tentando listar os atletas sem estar logado"""

    # O robô tenta dar um GET na rota trancada sem passar nenhum crachá
    response = client.get("/treinador/lista")

    # Verificamos se o segurança barrou ele com o código 401 (Não Autorizado)
    assert response.status_code == 401

    # Opcional: checar se a mensagem de erro está correta
    assert response.json() == {"detail": "Not authenticated"}


def test_criar_atleta_com_cracha_valido():
    """Simula o fluxo completo: Criar Treinador -> Logar -> Passar na Catraca -> Criar Atleta"""

    # 1. O robô cria um treinador novo no banco falso
    client.post(
        "/treinador",
        json={"nome_treinador": "Treinador_Teste", "senha": "senha_segura"},
    )

    # 2. O robô faz o login (ATENÇÃO: usando 'data' porque é um Formulário OAuth2!)
    resposta_login = client.post(
        "/login", data={"username": "Treinador_Teste", "password": "senha_segura"}
    )

    # Garantimos que o login deu certo
    assert resposta_login.status_code == 200

    # 3. O robô extrai o crachá (Token JWT) da resposta
    token = resposta_login.json()["access_token"]

    # 4. Preparamos o Cabeçalho (Headers) pendurando o crachá no formato Bearer
    cabecalho_de_seguranca = {"Authorization": f"Bearer {token}"}

    # 5. O robô bate na rota trancada, mostrando o crachá e enviando os dados do Atleta
    resposta_atleta = client.post(
        "/treinador/atleta",
        json={
            "nome_atleta": "Special Week",
            "status_velocidade": 35.5,
            "status_stamina": 85,
        },
        headers=cabecalho_de_seguranca,
    )

    # 6. O Teste de Ouro: O segurança abriu a catraca?
    assert resposta_atleta.status_code == 200
    assert resposta_atleta.json() == {
        "Mensagem": "Novo atleta adicionado com sucesso a lista"
    }

def test_listar_lista_com_cracha_valido():
    