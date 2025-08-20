from typing import Optional # deixar o item opcional ou não
from pydantic import BaseModel # 

class PersonagensToyStory(BaseModel):

    id: Optional[int] = None
    nome: str
    dono: str
    tamanho: str
    foto: str
