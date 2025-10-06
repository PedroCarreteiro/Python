from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.equipe_model import EquipeModel
from schemas.equipe_schema import EquipeSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EquipeSchema)
async def post_equipe(equipe: EquipeSchema, db: AsyncSession = Depends(get_session)):
    nova_equipe = EquipeModel(nome_equipe = equipe.nome_equipe,
                              nacionalidade_equipe = equipe.nacionalidade_equipe)
    
    db.add(nova_equipe)
    await db.commit()
    
    return nova_equipe

@router.get("/", response_model=List[EquipeSchema])
async def get_equipes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(EquipeModel)
        result = await session.execute(query)
        equipes: List[EquipeModel] = result.scalars().all()

        return equipes
    
@router.get("/{equipe_id}", response_model=EquipeSchema)
async def get_equipe(equipe_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(EquipeModel).filter(EquipeModel.id == equipe_id)
        result = await session.execute(query)
        equipe = result.scalar_one_or_none()

        if equipe:
            return equipe
        else:
            raise HTTPException(detail="Equipe não encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
@router.put("/{equipe_id}", response_model=EquipeSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_equipe(equipe_id: int, equipe: EquipeSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(EquipeModel).filter(EquipeModel.id == equipe_id)
        result = await session.execute(query)
        equipe_up = result.scalar_one_or_none()

        if equipe_up:
            equipe_up.nome_equipe = equipe.nome_equipe
            equipe_up.nacionalidade_equipe = equipe.nacionalidade_equipe

            await session.commit()
            
            return equipe_up
        
        else:
            raise HTTPException(detail="Equipe não encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{equipe_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_equipe(equipe_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(EquipeModel).filter(EquipeModel.id == equipe_id)
        result = await session.execute(query)
        equipe_del = result.scalar_one_or_none()

        if equipe_del:
            await session.delete(equipe_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Equipe não encontrada", status_code=status.HTTP_404_NOT_FOUND)
