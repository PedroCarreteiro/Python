from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.carro_model import CarroModel
from schemas.carro_schema import CarroSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CarroSchema)
async def post_carro(carro: CarroSchema, db: AsyncSession = Depends(get_session)):
    novo_carro = CarroModel(modelo_carro = carro.modelo_carro,
                            montadora = carro.montadora,
                            potencia = carro.potencia,
                            unidade_potencia = carro.unidade_potencia,
                            id_equipe = carro.id_equipe)
    db.add(novo_carro)
    await db.commit()

    return novo_carro

@router.get("/", response_model=List[CarroSchema])
async def get_carros(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroSchema)
        result = await session.execute(query)
        carros: List[CarroModel] = result.scalars().all()

        return carros
    
@router.get("/{id_carro}", response_model=CarroSchema)
async def get_carro(id_carro: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel).filter(CarroModel.id == id_carro)
        result = await session.execute(query)
        carro = result.scalar_one_or_none()

        if carro:
            return carro
        else:
            raise HTTPException(detail="Carro não encontrado", status_code=status.HTTP_404_NOT_FOUND)