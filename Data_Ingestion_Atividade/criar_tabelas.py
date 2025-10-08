from core.configs import settings
from core.database import engine
from models import __all__models  # Isso precisa estar devidamente configurado no seu projeto

import asyncio

async def create_tables() -> None:
    print("Criando as tabelas no banco de dados")

    # Criar um bloco de contexto assíncrono
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)  # Exclui tabelas antigas
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)  # Cria novas tabelas

    print("Tabelas criadas com sucesso")

if __name__ == '__main__':
    asyncio.run(create_tables())
