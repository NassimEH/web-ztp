"""Fichier de la definition de la base de données :
Création notre base de données sqlite asynchrone avec aiosqlite. 
Définition de procédure permetant d'appeler notre base de données. 
"""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine("sqlite+aiosqlite:///extended_db_file.dhcpo")
SessionLocal = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass

async def get_db():
    """Procédure permetant d'appeler notre base de données de manière asynchrone"""
    async with engine.begin() as db_connection:
        await db_connection.run_sync(Base.metadata.create_all)
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
