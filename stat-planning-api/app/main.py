from fastapi import FastAPI
from app.routes import membres, planning, stats, heures, alertes, parametres

app = FastAPI(title="Statistiques de Planification API")

# Include routers
app.include_router(membres.router, prefix="/membres")
app.include_router(planning.router, prefix="/planning")
app.include_router(stats.router, prefix="/stats")
app.include_router(heures.router, prefix="/heures")
app.include_router(alertes.router, prefix="/alertes")
app.include_router(parametres.router, prefix="/parametres")

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API Statistiques de Planification"}