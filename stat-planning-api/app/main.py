from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import membres, planning, stats, heures, alertes, parametres, test

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(membres.router)
app.include_router(planning.router)
app.include_router(stats.router)
app.include_router(heures.router)
app.include_router(alertes.router)
app.include_router(parametres.router)
app.include_router(test.router)

@app.get("/")
async def root():
    return {"message": "Stat Planning API en ligne"}
