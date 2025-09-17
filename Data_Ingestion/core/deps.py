from  typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        #yield: tenta retornar a sessão e não finaliza ele direto, sem ir para a outra parte
        yield session
    finally:
        await session.close()

