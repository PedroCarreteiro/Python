from typing import Optional
from pydantic import BaseModel as SCBaseModel

class EquipeSchema(SCBaseModel):
    
    id: Optional[int] = None
    noome_equipe: str
    nacionalidade_equipe: str

    class Config:
        orm_mode = True