
from fastapi import APIRouter
from app.services.rentman import fetch_heures_planifiees, fetch_heures_effectuees

router = APIRouter()

@router.get("/planifiees")
async def get_heures_planifiees():
    return await fetch_heures_planifiees()

@router.get("/effectuees")
async def get_heures_effectuees():
    return await fetch_heures_effectuees()
