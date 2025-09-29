from core.configs import settings
from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey

class EquipeModel(settings.DBBaseModel):
    __tablename__ = 'equipe'

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome_equipe: str = Column(String(100))
    nacionalidade_equipe: str = Column(String(100))