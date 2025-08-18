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
