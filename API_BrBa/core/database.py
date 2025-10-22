from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings 

#sessionmaker retorna uma classe
#ele vai abrir e fechar a conexão com o banco de dados

engine: AsyncEngine = create_async_engine(settings.DB_URL)
Session: AsyncEngine = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine)
