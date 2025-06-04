import os
import httpx
from typing import List, Dict

RENTMAN_API_URL = "https://api.rentman.net/functions"
RENTMAN_TOKEN = os.getenv("RENTMAN_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {RENTMAN_TOKEN}",
    "Content-Type": "application/json"
}

async def fetch_heures_planifiees() -> List[Dict]:
    payload = {
        "action": "read",
        "module": "functions",
        "parameters": {
            "filter": {
                "start_time": {
                    "gte": "2024-01-01T00:00:00Z"
                }
            },
            "fields": ["start_time", "end_time", "function_id", "crew_members"]
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(RENTMAN_API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json().get("data", [])

async def fetch_heures_effectuees() -> List[Dict]:
    payload = {
        "action": "read",
        "module": "functions",
        "parameters": {
            "filter": {
                "start_time": {
                    "gte": "2024-01-01T00:00:00Z"
                }
            },
            "fields": ["start_time", "end_time", "function_id", "crew_members"]
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(RENTMAN_API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json().get("data", [])
