from fastapi import APIRouter, HTTPException
from app.services.rentman import fetch_heures_planifiees, fetch_heures_effectuees

router = APIRouter()

@router.get("/")
async def get_statistiques():
    try:
        planifiees = await fetch_heures_planifiees()
        effectuees = await fetch_heures_effectuees()
    except Exception as e:
        print(f"❌ ERREUR API Rentman : {e}")
        raise HTTPException(status_code=500, detail=f"Erreur API Rentman: {str(e)}")

    stats = {}

    def extract_info(fonction):
        employes = fonction.get("crew_members", [])
        duree = 0
        start = fonction.get("start_time")
        end = fonction.get("end_time")
        if start and end and len(start) >= 16 and len(end) >= 16:
            from datetime import datetime
            start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
            end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
            duree = (end_dt - start_dt).total_seconds() / 3600
        mois = start[:7] if start else "unknown"
        return employes, mois, duree

    for fonction in planifiees:
        employes, mois, duree = extract_info(fonction)
        for emp in employes:
            stats.setdefault((emp, mois), {"heures_planifiees": 0, "heures_effectuees": 0})
            stats[(emp, mois)]["heures_planifiees"] += duree

    for fonction in effectuees:
        employes, mois, duree = extract_info(fonction)
        for emp in employes:
            stats.setdefault((emp, mois), {"heures_planifiees": 0, "heures_effectuees": 0})
            stats[(emp, mois)]["heures_effectuees"] += duree

    result = []
    for (emp, mois), values in stats.items():
        depassement = "Oui" if values["heures_planifiees"] > 151.67 else "Non"
        result.append({
            "employe_id": emp,
            "mois": mois,
            **values,
            "depassement_quota": depassement
        })

    return result
