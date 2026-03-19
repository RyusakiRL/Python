"""Molde de dados do SQL"""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Boolean, Integer, String, Float, ForeignKey

Base = declarative_base()


class Preset(Base):
    """Modelagem de dados dos presets"""

    __tablename__ = "presets"
    id = Column(Integer, primary_key=True, index=True)
    nome_musica = Column(String, index=True, nullable=False, unique=True)
    software_usado = Column(String, nullable=False)
    nivel_ganho = Column(Float, nullable=False)
    distorcao = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("produtor.id"), nullable=False)
    user = relationship("Produtor", back_populates="presets")


class Produtor(Base):
    """Modelagem de dados do produtor"""

    __tablename__ = "produtor"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    presets = relationship("Preset", back_populates="user")
