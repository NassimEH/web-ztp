"""Fichier pour lancer le serveur fastapi"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from sqlalchemy import select

from db.database import get_db
from db.models import Device, Template, DHCPConfig
from db.schema import DeviceSchema, TemplateSchema, DHCPConfigSchema

from env import FRONTEND_URL


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=[FRONTEND_URL], allow_credentials=True)

## Device endpoints


@app.post("/device", response_model=DeviceSchema)
def add_device(device: DeviceSchema, db: Session = Depends(get_db)):
    """Permet d'ajouter un device à la bdd"""
    new_device = Device(
        serial_number=device.serial_number,
        ip=str(device.ip),
        hostname=device.hostname,
        interface=device.interface,
        template_id=device.template_id,
    )
    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    return new_device


@app.get("/devices")
def get_devices(db: Session = Depends(get_db)):
    """Recupère la liste des devices"""
    results = db.execute(select(Device))
    devices = results.scalars().all()

    return devices


@app.get("/device/{device_id}")
def get_device(device_id: int, db: Session = Depends(get_db)):
    """Recupère un device"""
    device = db.get(Device, device_id)

    return device


@app.get("/ip/{device_serial_number}")
def get_ip(device_serial_number: str, db: Session = Depends(get_db)):
    """Recupère l'ip d'un device à partir de son serial number"""
    device = db.get(Device, device_serial_number)

    return device.ip


@app.get("/ips")
def get_ips(db: Session = Depends(get_db)):
    """Recupère la liste des ips"""
    results = db.execute(select(Device.ip))
    ips = results.scalars().all()

    return ips


@app.post("/template", response_model=TemplateSchema)
def add_template(template: TemplateSchema, db: Session = Depends(get_db)):
    """Permet d'ajouter un template à la bdd"""
    new_template = Template(
        file_path=template.file_path,
    )
    db.add(new_template)
    db.commit()
    db.refresh(new_template)

    return new_template


## Template endpoints


@app.get("/templates")
def get_templates(db: Session = Depends(get_db)):
    """Recupère la liste des templates"""
    results = db.execute(select(Template))
    templates = results.scalars().all()

    return templates


@app.get("/template/{template_id}")
def get_template(template_id: int, db: Session = Depends(get_db)):
    """Recupère un template"""
    template = db.get(Template, template_id)

    return template


## DHCP server endpoints


@app.post("/dhcpconfig", response_model=DHCPConfigSchema)
def add_dhcpconfig(dhcpconfig: DHCPConfigSchema, db: Session = Depends(get_db)):
    """Permet d'ajouter une configuration DHCP à la bdd"""
    new_dhcpconfig = DHCPConfig(
        subnet=str(dhcpconfig.subnet),
        min_ip_pool=str(dhcpconfig.min_ip_pool),
        max_ip_pool=str(dhcpconfig.max_ip_pool),
    )
    db.add(new_dhcpconfig)
    db.commit()
    db.refresh(new_dhcpconfig)

    return new_dhcpconfig


@app.patch("/dhcpconfig", response_model=DHCPConfigSchema)
def update_dhcpconfig(dhcpconfig: DHCPConfigSchema, db: Session = Depends(get_db)):
    """Permet de mettre à jour la configuration DHCP"""
    new_dhcpconfig = DHCPConfig(
        subnet=str(dhcpconfig.subnet),
        min_ip_pool=str(dhcpconfig.min_ip_pool),
        max_ip_pool=str(dhcpconfig.max_ip_pool),
    )
    db.update(new_dhcpconfig)
    db.commit()
    db.refresh(new_dhcpconfig)

    return new_dhcpconfig


@app.get("/dhcpconfig")
def get_dhcpconfig(db: Session = Depends(get_db)):
    """Recupère la configuration DHCP"""
    dhcp = db.get(DHCPConfig, 1)

    return dhcp


@app.get("/subnet")
def get_subnet(db: Session = Depends(get_db)):
    """Recupère la subnet"""
    dhcp = db.get(DHCPConfig, 1)

    return dhcp.subnet


@app.get("/min_ip_pool")
def get_min_ip_pool(db: Session = Depends(get_db)):
    """Recupère la min_ip_pool"""
    dhcp = db.get(DHCPConfig, 1)

    return dhcp.min_ip_pool


@app.get("/max_ip_pool")
def get_max_ip_pool(db: Session = Depends(get_db)):
    """Recupère la max_ip_pool"""
    dhcp = db.get(DHCPConfig, 1)

    return dhcp.max_ip_pool
