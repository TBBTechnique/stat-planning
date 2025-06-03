from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_planning():
    return {"planning": "A implémenter"}