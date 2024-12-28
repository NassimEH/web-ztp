from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
import os

db_path = os.path.join(os.path.dirname(__file__), 'ztp.db')
engine = create_engine(f'sqlite:///{db_path}')
Base = declarative_base()

# Supprime le fichier ztp.db s'il existe et le recrée
if os.path.exists(db_path):
    os.remove(db_path)
Base.metadata.create_all(engine)

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String, unique=True, nullable=False)
    hostname = Column(String, nullable=False)
    ip_management = Column(String, nullable=False)
    credentials = Column(String, nullable=False)
    interface_config = Column(String)
    template_id = Column(Integer, ForeignKey('templates.id'))
    template = relationship("Template", back_populates="devices")
#Chaque équipement de la table Device doit avoir un template_id pointant vers l'ID du modèle dans la table Template. 
#permet de définir quel modèle est utilisé pour configurer cet équipement.

class Template(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    devices = relationship("Device", back_populates="template")


class Variable(Base):
    __tablename__ = 'variables'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'))
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Session pour interagir avec la base
Session = sessionmaker(bind=engine)
session = Session()

# Variables de tests
new_template = Template(
    name="Default Template",
    content="interface {interface}\n ip address {ip_management}\n hostname {hostname}\n"
)
new_device = Device(
    serial_number="SN123456789",
    hostname="Switch01",
    ip_management="192.168.1.1",
    credentials="admin:password",
    interface_config="GigabitEthernet0/1",
    template=new_template
)
new_variable1 = Variable(device_id=1, key="interface", value="GigabitEthernet0/1")
new_variable2 = Variable(device_id=1, key="ip_management", value="192.168.1.1")
new_variable3 = Variable(device_id=1, key="hostname", value="Switch01")

# Commit dans les tables
session.add(new_template)
session.add(new_device)
session.add_all([new_variable1, new_variable2, new_variable3])
session.commit()

# Lecture des données
templates = session.query(Template).all()
devices = session.query(Device).all()
variables = session.query(Variable).all()

print("--------------------------- Contenu de la table Templates : ---------------------------")
for template in templates:
    print(template.id, template.name, template.content)

print("--------------------------- Contenu de la table Devices : -----------------------------")
for device in devices:
    print(device.id, device.serial_number, device.hostname, device.ip_management, device.credentials, device.interface_config, device.template.name)

print("--------------------------- Contenu de la table Variables : ---------------------------")
for variable in variables:
    print(variable.device_id, variable.key, variable.value)

print("--------------------------- Exemple de configuration ZTP : ---------------------------")

# Récupérer un équipement spécifique
device = session.query(Device).filter_by(serial_number="SN123456789").first()

# Récupérer le modèle associé
template = session.query(Template).filter_by(id=device.template_id).first()

# Récupérer les variables associées à cet équipement
variables = session.query(Variable).filter_by(device_id=device.id).all()

# Charger le contenu du modèle
template_content = template.content

# Remplacer les placeholders par les valeurs des variables
for variable in variables:
    placeholder = f"{{{variable.key}}}"  # Format du placeholder dans le template
    template_content = template_content.replace(placeholder, variable.value)

# Résultat final
print("Configuration générée :")
print(template_content)
