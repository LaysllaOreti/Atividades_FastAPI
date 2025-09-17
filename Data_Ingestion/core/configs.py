from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

# coloca as configurações do projeto, passa por herança para ter todas as configurações
class Settings(BaseSettings):

    #variavel de versionamento em casos necessários
    API_V1_STR: str = "/api/v1"
    #API_V2_STR: str = "/api/v2"

    # todos os models herdem os recursos do sqlachemy, padronizado
    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3306/bandas"

    DBBaseModel = declarative_base()

class Config:
    # não ficar dando erro em arquivos sensiveis, ignora
    case_sensitive = False
    env_file = "env"

# importa a variavel que herda a classe
settings = Settings()