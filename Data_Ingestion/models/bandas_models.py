from core.configs import settings
from sqlalchemy import Column, Integer, String, Float, Boolean

class BandasModel(settings.DBBaseModel):
    __tablename__ = "bandas"

    # a STRING suporta até 256 caracteres
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(80))
    qnt_integrantes: int = Column(Integer())
    tipo_musical: str = Column(String(50))
