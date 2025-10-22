from core.configs import settings 
from core.database import engine
from models import __all__models

async def create_tables() -> None:
    print("Criando as tabelas no banco de dados")
#criar um bloco de contexto assíncrono
    async with engine.begin() as conn:
        await conn.run_sync (settings.DBBaseModel.metadata.drop_all)
#excluir, caso já exista
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso!')

if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())