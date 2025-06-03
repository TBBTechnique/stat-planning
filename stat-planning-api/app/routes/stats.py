
from fastapi import APIRouter
from app.services.rentman import fetch_heures_planifiees, fetch_heures_effectuees

router = APIRouter()

@router.get("/")
async def get_statistiques():
    planifiees = await fetch_heures_planifiees()
    effectuees = await fetch_heures_effectuees()

    stats = {}

    for heure in planifiees:
        emp = heure["employe_id"]
        mois = heure["date"][:7]
        stats.setdefault((emp, mois), {"heures_planifiees": 0, "heures_effectuees": 0})
        stats[(emp, mois)]["heures_planifiees"] += heure["duree_h"]

    for heure in effectuees:
        emp = heure["employe_id"]
        mois = heure["date"][:7]
        stats.setdefault((emp, mois), {"heures_planifiees": 0, "heures_effectuees": 0})
        stats[(emp, mois)]["heures_effectuees"] += heure["duree_h"]

    result = []
    for (emp, mois), values in stats.items():
        depassement = "Oui" if values["heures_planifiees"] > 151.67 else "Non"  # quota approx. 35h x 4.33
        result.append({
            "employe_id": emp,
            "mois": mois,
            **values,
            "depassement_quota": depassement
        })

    return result
