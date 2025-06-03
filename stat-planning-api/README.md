# Statistiques de Planification API

Une API FastAPI pour suivre les heures planifiées et effectuées via Rentman.

## Lancer en local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Déploiement Render

- Ajouter `RENTMAN_TOKEN` dans les variables d’environnement Render.
- Push sur GitHub et connecter au service Render.