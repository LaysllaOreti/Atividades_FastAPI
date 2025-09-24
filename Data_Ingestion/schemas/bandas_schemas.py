from typing import Optional
from pydantic import BaseModel as SCBaseModel

class BandasSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    qtd_integrantes: int
    tipo_musical: str

    class Config:
        # Será em formato JSON, porém estará conectado com o banco de dados
        orm_model = True