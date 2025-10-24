# setamos o banco que será utilizado

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

# de core.configs importamos a variável settings
from core.configs import settings


# este código é responsável por abrir e fechar a conexão com o banco de dados

# variável que recebe o objeto AsyncEngine
engine: AsyncEngine = create_async_engine(settings.DB_URL)

# sessionmaker retorna uma classe de sessão configurada
Session: AsyncEngine = sessionmaker(
    # evita que o commit seja executado automaticamente
    autocommit=False,

    # evita o envio automático dos dados sem sinal explícito
    autoflush=False,

    # impede que os objetos expirem após o commit
    expire_on_commit=False,

    # define o uso de sessões assíncronas
    class_=AsyncSession,

    # vincula a sessão ao engine configurado
    bind=engine
)
