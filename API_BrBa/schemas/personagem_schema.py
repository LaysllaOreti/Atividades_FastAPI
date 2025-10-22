from typing import Optional
from pydantic import BaseModel as SCBBaseModel
#como o SQL Alchemy tem o BaseModel dele, não podemos confundir

class PersonagemSchema(SCBBaseModel):
    id: Optional[int] = None
    nome: str 
    apelido: str 
    idade: int 
    ocupacao: str

class Config:
    orm_mode = True