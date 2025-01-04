"""Fichier de la definition de la base de données :
Création notre base de données sqlite asynchrone avec aiosqlite. 
Définition de procédure permetant d'appeler notre base de données. 
"""

from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///ztp_config.db")
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

def get_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
