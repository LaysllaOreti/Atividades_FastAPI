from core.configs import settings
# importamos os tipos de dados e colunas que serão usados no banco
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import Optional

# DBBaseModel é a classe declarativa do SQLAlchemy

# cria a classe PersonagensModel que herda de DBBaseModel definido em settings
class PersonagensModel(settings.DBBaseModel):
    # define o nome da tabela no banco de dados
    __tablename__ = "personagensbrba"

    # define os campos da tabela
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    # campo que não pode ser nulo
    nome: str = Column(String(255), nullable=False)
    idade: int = Column(Integer())
    ocupacao: str = Column(String(255), nullable=False)


# cria a classe PersonagensSchemaPatch para atualizações parciais (PATCH)
class PersonagensSchemaPatch(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    ocupacao: Optional[str] = None

    class Config:
        from_attributes = True
