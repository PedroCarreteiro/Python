from core.configs import settings
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

class CarroModel(settings.DBBaseModel):
    __tablename__ = 'carro'

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    modelo_carro: str = Column(String(100))
    montadora: str = Column(String(100))
    potencia: float = Column(Float())
    unidade_potencia: str = Column(String(100))
    id_equipe:int = Column(Integer, ForeignKey('equipe.id'))

