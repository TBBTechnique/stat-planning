from fastapi import APIRouter
from app.services.rentman import fetch_crew_data

router = APIRouter()

@router.get("/")
async def get_membres():
    membres = await fetch_crew_data()
    return membres