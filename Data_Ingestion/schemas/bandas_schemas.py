from typing import Optional
from pydantic import BaseModel as SCBaseModel #"trocar" o nome dele somente aqui

class BandaSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    qnt_integrantes: int
    tipo_musical: str

    class Config:
        orm_mode = True