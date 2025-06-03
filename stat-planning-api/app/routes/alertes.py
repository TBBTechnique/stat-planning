
from fastapi import APIRouter
from app.routes.stats import get_statistiques

router = APIRouter()

@router.get("/")
async def get_alertes():
    stats = await get_statistiques()
    alertes = [s for s in stats if s["depassement_quota"] == "Oui"]
    return alertes
