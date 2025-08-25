from typing import Optional
from pydantic import BaseModel

class Carro(BaseModel):
    id: Optional[int] = None
    equipe: str
    marca: str
    modelo: str
    potencia: int
    cambio: str
    tracao: str
    pneus: str
    combustivel: int

class CarroPatch(BaseModel):
    id: Optional[int] = None
    equipe : Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    potencia: Optional[int] = None
    cambio: Optional[str] = None
    tracao: Optional[str] = None
    pneus: Optional[str] = None
    combustivel: Optional[int] = None
    
