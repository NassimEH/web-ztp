"""Fichier temporaire"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import os

# Mise en place de la base de donnée
db_path = os.path.join(os.path.dirname(__file__), 'dhcp.db')
engine = create_engine(f'sqlite:///{db_path}')# Base SQLite
Base = declarative_base()  # Définition des modèles

#Une table "pool(subnet,masque,@ip_debut, @ip_fin, dns et gateway ?)"
#"Baux(client, temps_début, temps_fin, status)"
# "clients(@mac,@ip)"
class Pool(Base):
    __tablename__ = 'pool'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subnet = Column(String)
    masque = Column(String)
    ip_debut = Column(String)
    ip_fin = Column(String)

class Baux(Base):
    __tablename__ = 'baux'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client = Column(String, ForeignKey('clients.mac'))
    temps_debut = Column(DateTime)
    temps_fin = Column(DateTime, default=datetime.utcnow)
    status = Column(String)

class Clients(Base):
    __tablename__ = 'clients'
    mac = Column(String, primary_key=True)
    ip = Column(String)

Base.metadata.create_all(engine) # Création de la base

# Session pour interagir avec la base
Session = sessionmaker(bind=engine)
session = Session()

#VARIABLES DE TESTS
new_pool = Pool(subnet = "1.1.1.0",
    masque = "/24",
    ip_debut = "1.1.1.1",
    ip_fin = "1.1.1.254")
new_bail = Baux(client = "a.b.c.d.e.f.g.P", temps_fin = datetime(2024, 11, 26, 20, 0, 0),
                 status = "actif")
new_client = Clients(mac = "a.b.c.d.e.f.g.P",
                    ip = "1.1.1.4")

#COMMIT DANS LES TABLES
session.add(new_pool)
session.add(new_bail)
session.add(new_client)
session.commit()

# Lecture
ip = session.query(Pool).all()
baux = session.query(Baux).all()
clients = session.query(Clients).all()
print("----------------------------------- Contenu de la table Pool : --------------------------------------")
for adresse in ip:
    print(adresse.id, adresse.subnet, adresse.masque, adresse.ip_debut, adresse.ip_fin)

print("----------------------------------- Contenu de la table Baux : --------------------------------------")
for bail in baux :
    print(bail.id, bail.client, bail.temps_debut, bail.temps_fin, bail.status)

print("----------------------------------- Contenu de la table Clients : -----------------------------------")
for client in clients :
    print(client.mac, client.ip)

