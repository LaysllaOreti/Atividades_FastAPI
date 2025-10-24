# código simples para verificar e criar as tabelas no banco

from core.configs import settings
from core.database import engine
from models import all_models

async def create_table() -> None:
    print("criando as tabelas no banco da API BrBa...")

    async with engine.begin() as conn:
        # cria um bloco de contexto assíncrono
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        # exclui as tabelas existentes (caso já existam)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    
    print("tabelas criadas com sucesso!")


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_table())
