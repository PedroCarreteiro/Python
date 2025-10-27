from fastapi import APIRouter
from api.v1.endpoints import turmas
from api.v1.endpoints import file

api_router = APIRouter()

api_router.include_router(turmas.router, prefix="/turmas", tags=["Turmas"])

api_router.include_router(file.router, prefix="/files", tags=["Files"])
