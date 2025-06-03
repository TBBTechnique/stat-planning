from fastapi import APIRouter, HTTPException
from app.services.rentman import fetch_heures_planifiees, fetch_heures_effectuees

router = APIRouter()

@router.get("/")
async def get_statistiques():
    try:
        planifiees = await fetch_heures_planifiees()
        effectuees = await fetch_heures_effectuees()
    except Exception as e:
        print(f"❌ ERREUR LORS DES APPELS RENTMAN : {e}")
        raise HTTPException(status_code=500, detail=f"Erreur API Rentman: {str(e)}")

    stats = {}

    try:
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
            depassement = "Oui" if values["heures_planifiees"] > 151.67 else "Non"
            result.append({
                "employe_id": emp,
                "mois": mois,
                **values,
                "depassement_quota": depassement
            })

        return result

    except Exception as e:
        print(f"❌ ERREUR DANS LE TRAITEMENT DES DONNÉES : {e}")
        raise HTTPException(status_code=500, detail=f"Erreur traitement: {str(e)}")


    return result
