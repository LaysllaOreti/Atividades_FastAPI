from core.configs import settings 
from sqlalchemy import Column, Integer, String

#DBBaseModel é a classe declarativa do SQL Alchemy

class PersonagemModel (settings.DBBaseModel) :
    __tablename__ = "personagens"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    apelido: str = Column(String(85))
    idade: int = Column(Integer)
    ocupacao: str = Column(String(100))
    