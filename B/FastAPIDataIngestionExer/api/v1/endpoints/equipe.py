from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.equipe_model import EquipeModel
from schemas.equipe_schema import EquipeSchema
from core.deps import get_session
