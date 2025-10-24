# abre e fecha a conexão com o banco para realizar a injeção de dependência

from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

# função responsável por fornecer uma sessão para operações no banco (GET, POST, etc.)
async def get_session() -> Generator:
    session: AsyncSession = Session()

    # tenta criar e usar a sessão
    try:
        # retorna a sessão ativa para ser utilizada nos endpoints
        yield session
    # ao final da execução, fecha a conexão com o banco
    finally:
        await session.close()
