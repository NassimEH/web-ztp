"""Fichier contenant le modele de données de l'ORM"""

from .database import Base 

from sqlalchemy.orm import Mapped, mapped_column

class Client(Base):
    """Client DHCP"""
    __tablename__ = 'clients'
    mac: Mapped[str] = mapped_column(primary_key=True)
    ip: Mapped[str] = mapped_column(unique=True)
    hostname: Mapped[str] = mapped_column(nullable=True)