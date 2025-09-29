from fastapi import APIRouter
from api.v1.endpoints import carro
from api.v1.endpoints import equipe

api_router = APIRouter()

api_router.include_router(carro.router, prefix="/carro", tags=["Carro"])
api_router.include_router(equipe.router, prefix="/equipe", tags=["Equipe"])