from typing import Optional
from pydantic import BaseModel as SCBaseModel

# Como o SQLAlchemy tem o BaseModel dele, não podemos confundir com o do Pydantic
class CursoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    produtora: str
    atores_principais: str
    horas_filme: int

    class Config:
        orm_mode = True
