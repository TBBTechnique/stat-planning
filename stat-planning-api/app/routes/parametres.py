
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models import Parametres
from app.database import engine

router = APIRouter()

@router.get("/")
def get_parametres():
    with Session(engine) as session:
        param = session.exec(select(Parametres)).first()
        if not param:
            param = Parametres()
            session.add(param)
            session.commit()
            session.refresh(param)
        return param

@router.put("/")
def update_parametres(p: Parametres):
    with Session(engine) as session:
        existing = session.exec(select(Parametres).where(Parametres.id == 1)).first()
        if not existing:
            raise HTTPException(status_code=404, detail="Paramètres non trouvés.")
        for key, value in p.dict().items():
            setattr(existing, key, value)
        session.add(existing)
        session.commit()
        session.refresh(existing)
        return existing
