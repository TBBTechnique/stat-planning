from fastapi import APIRouter, HTTPException
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

RENTMAN_API_URL = "https://api.rentman.net/crew"
RENTMAN_TOKEN = os.getenv("RENTMAN_API_TOKEN")

@router.get("/test-crew")
async def test_rentman_crew():
    headers = {
        "Authorization": f"Bearer {RENTMAN_TOKEN}",
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(RENTMAN_API_URL, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Erreur API Rentman: {response.text}")

    return response.json()
