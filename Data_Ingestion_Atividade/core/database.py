from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

# sessionmaker retorna uma classe para criar sessões com o banco de dados
# Ele é responsável por abrir e fechar conexões

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)
