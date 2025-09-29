from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CarroSchema(SCBaseModel):

    id: Optional[int] = None
    modelo_carro: str
    montadora: str
    potencia: float
    unidade_potencia: str
    id_equipe: int

    class Config:
        orm_mode = True

