from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from db.database import get_db
from db.models import Device
from db.schema import DeviceSchema

router = APIRouter(prefix="/device", tags=["Devices"])

@router.post("/", response_model=DeviceSchema)
def add_device(device: DeviceSchema, db: Session = Depends(get_db)):
    """Ajoute un device à la base de données"""
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

@router.get("s")
def get_devices(db: Session = Depends(get_db)):
    """Récupère la liste des devices"""
    results = db.execute(select(Device))
    return results.scalars().all()

@router.get("/{device_id}")
def get_device(device_id: int, db: Session = Depends(get_db)):
    """Récupère un device par son ID"""
    return db.get(Device, device_id)

@router.get("/ip/{device_serial_number}")
def get_ip(device_serial_number: str, db: Session = Depends(get_db)):
    """Récupère l'IP d'un device via son numéro de série"""
    device = db.get(Device, device_serial_number)
    return device.ip if device else None

@router.get("/ips")
def get_ips(db: Session = Depends(get_db)):
    """Récupère la liste des IPs"""
    results = db.execute(select(Device.ip))
    return results.scalars().all()
