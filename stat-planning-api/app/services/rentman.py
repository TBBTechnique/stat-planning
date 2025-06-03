import os
import httpx
from dotenv import load_dotenv

load_dotenv()

RENTMAN_TOKEN = os.getenv("RENTMAN_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {RENTMAN_TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "StatPlanningApp/1.0"
}

BASE_URL = "https://api.rentman.net"

async def fetch_crew_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/crew", headers=HEADERS)
        response.raise_for_status()
        return response.json()

async def fetch_heures_planifiees():
    url = f"{BASE_URL}/functions"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        enriched = []
        for item in data.get("data", []):
            debut = item.get("start_time")
            fin = item.get("end_time")
            employe_id = item.get("crew_id")
            date = debut.split("T")[0] if debut else None

            if debut and fin:
                calc = calculer_duree_et_majoration(debut, fin)
                enriched.append({
                    "employe_id": employe_id,
                    "date": date,
                    "heure_debut": debut,
                    "heure_fin": fin,
                    **calc
                })

        return enriched


async def fetch_heures_effectuees():
    url = f"{BASE_URL}/timeregistration"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        enriched = []
        for item in data.get("data", []):
            debut = item.get("start_time")
            fin = item.get("end_time")
            employe_id = item.get("crew_id")
            date = debut.split("T")[0] if debut else None

            if debut and fin:
                calc = calculer_duree_et_majoration(debut, fin)
                enriched.append({
                    "employe_id": employe_id,
                    "date": date,
                    "heure_debut": debut,
                    "heure_fin": fin,
                    **calc
                })

        return enriched

from sqlmodel import Session, select
from app.database import engine
from app.models import Parametres

def get_parametres():
    with Session(engine) as session:
        param = session.exec(select(Parametres).where(Parametres.id == 1)).first()
        if not param:
            param = Parametres()
            session.add(param)
            session.commit()
            session.refresh(param)
        return param

def calculer_duree_et_majoration(start: str, end: str):
    fmt = "%Y-%m-%dT%H:%M:%S%z"
    dt_start = datetime.strptime(start, fmt)
    dt_end = datetime.strptime(end, fmt)
    duree_h = (dt_end - dt_start).total_seconds() / 3600
    jour = dt_start.weekday()
    heure_debut = dt_start.hour

    param = get_parametres()
    jours_actifs = [
        param.lundi_active,
        param.mardi_active,
        param.mercredi_active,
        param.jeudi_active,
        param.vendredi_active,
        param.samedi_active,
        param.dimanche_active
    ]

    majoration = "Non"
    raison = ""

    if jours_actifs[jour]:
        majoration = "Oui"
        raison = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"][jour]

    if (
        param.nuit_debut <= heure_debut or heure_debut < param.nuit_fin
        and param.taux_nuit > 0
    ):
        majoration = "Oui"
        raison = "Nuit"

    return {
        "duree_h": round(duree_h, 2),
        "jour": jour,
        "majoration": majoration,
        "raison": raison
    }