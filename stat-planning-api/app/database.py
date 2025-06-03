from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./statplan.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    from app.models import Member  # importer tous les modèles ici
    SQLModel.metadata.create_all(engine)