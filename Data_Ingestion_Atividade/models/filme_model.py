from core.configs import settings
from sqlalchemy import Column, Integer, String

# DBBaseModel é a classe declarativa do SQLAlchemy

class FilmeModel(settings.DBBaseModel):
    __tablename__ = 'filmes'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    produtora: str = Column(String(100))
    atores_principais: str = Column(String(100))
    horas_filme: int = Column(Integer)
