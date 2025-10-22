from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    """
    configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3306/faculdade'
    DBBaseModel = declarative_base() #serve para que os models herdem todos os recursos do sqlalchemy