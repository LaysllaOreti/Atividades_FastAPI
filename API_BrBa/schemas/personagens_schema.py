# converte os dados para JSON para permitir a comunicação com o banco
from typing import Optional
# como o SQLAlchemy também possui um BaseModel, usamos "as" para renomear o do Pydantic e evitar confusão
from pydantic import BaseModel as SCBaseModel

# garante que a requisição siga os mesmos campos definidos no model
class PersonagensSchema(SCBaseModel):
    # pode estar ausente ou ter valor None
    id: Optional[int] = None
    nome: str
    idade: int
    ocupacao: str

    class Config:
        # define que o schema será convertido para JSON para comunicação com o banco
        from_attributes = True
