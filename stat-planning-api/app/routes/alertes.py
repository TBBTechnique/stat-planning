from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_alertes():
    return [{"id": 1, "type": "Heures dépassées"}]