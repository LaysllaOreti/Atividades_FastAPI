from typing import Optional # deixa o item opcional ou não
from pydantic import BaseModel

class PersonagensOIncrivelMundoDeGumball(BaseModel):

    id: Optional[int] = None
    nome: str
    idade: int
    trabalho: str
    frase: str
    foto: str
