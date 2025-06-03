from sqlmodel import SQLModel, Field
from typing import Optional

class Member(SQLModel, table=True):
    id: str = Field(primary_key=True)
    nom: str
    contrat: Optional[str]
    taux_travail: Optional[float]

class HeurePlanifiee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employe_id: str
    date: str
    heure_debut: str
    heure_fin: str
    duree_h: Optional[float] = None
    jour_semaine: Optional[int] = None
    majoration: Optional[str] = None
    raison_majoration: Optional[str] = None

class HeureEffectuee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employe_id: str
    date: str
    heure_debut: str
    heure_fin: str
    duree_h: Optional[float] = None
    jour_semaine: Optional[int] = None
    majoration: Optional[str] = None
    raison_majoration: Optional[str] = None


class Parametres(SQLModel, table=True):
    id: Optional[int] = Field(default=1, primary_key=True)
    nuit_debut: int = 22
    nuit_fin: int = 5
    taux_nuit: float = 25.0
    taux_dimanche: float = 25.0
    lundi_active: bool = False
    mardi_active: bool = False
    mercredi_active: bool = False
    jeudi_active: bool = False
    vendredi_active: bool = False
    samedi_active: bool = False
    dimanche_active: bool = True
