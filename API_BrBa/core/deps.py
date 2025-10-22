from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> Generator: #função que vai ter como retorno um Generator
    session: AsyncSession = Session()
    try:
        yield session 
    finally:
        await session.close() # após a sessão com o banco, ai sim fechamos ela