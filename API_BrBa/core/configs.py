# dentro do módulo colocamos as configurações do banco

from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base


# crio a classe que herda de BaseSettings
class Settings(BaseSettings):
    # configurações gerais usadas na aplicação, incluindo o caminho base da API

    # variável de versionamento
    API_V1_STR: str = '/api/v1'

    # configuração da conexão com o banco de dados (neste caso, MySQL)
    # altere a porta se necessário
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3306/personagensbrba'

    # padronização para que todos os models herdem os recursos do SQLAlchemy
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = False
        env_file = ".env"


# aqui estamos definindo a variável que herda a classe Settings (que herda BaseSettings)
settings = Settings()
