from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import DHCPConfig
from db.schema import DHCPConfigSchema

router = APIRouter(prefix="/dhcpconfig", tags=["DHCP Config"])

@router.post("/", response_model=DHCPConfigSchema)
def add_dhcpconfig(dhcpconfig: DHCPConfigSchema, db: Session = Depends(get_db)):
    """Ajoute une configuration DHCP à la base de données"""
    new_dhcpconfig = DHCPConfig(
        subnet=str(dhcpconfig.subnet),
        min_ip_pool=str(dhcpconfig.min_ip_pool),
        max_ip_pool=str(dhcpconfig.max_ip_pool),
    )
    db.add(new_dhcpconfig)
    db.commit()
    db.refresh(new_dhcpconfig)
    return new_dhcpconfig

@router.patch("/", response_model=DHCPConfigSchema)
def update_dhcpconfig(dhcpconfig: DHCPConfigSchema, db: Session = Depends(get_db)):
    """Met à jour la configuration DHCP"""
    dhcp = db.get(DHCPConfig, 1)
    if dhcp:
        dhcp.subnet = str(dhcpconfig.subnet)
        dhcp.min_ip_pool = str(dhcpconfig.min_ip_pool)
        dhcp.max_ip_pool = str(dhcpconfig.max_ip_pool)
        db.commit()
        db.refresh(dhcp)
    return dhcp

@router.get("/")
def get_dhcpconfig(db: Session = Depends(get_db)):
    """Récupère la configuration DHCP"""
    return db.get(DHCPConfig, 1)

@router.get("/subnet")
def get_subnet(db: Session = Depends(get_db)):
    """Récupère le subnet"""
    dhcp = db.get(DHCPConfig, 1)
    return dhcp.subnet if dhcp else None

@router.get("/min_ip_pool")
def get_min_ip_pool(db: Session = Depends(get_db)):
    """Récupère la min_ip_pool"""
    dhcp = db.get(DHCPConfig, 1)
    return dhcp.min_ip_pool if dhcp else None

@router.get("/max_ip_pool")
def get_max_ip_pool(db: Session = Depends(get_db)):
    """Récupère la max_ip_pool"""
    dhcp = db.get(DHCPConfig, 1)
    return dhcp.max_ip_pool if dhcp else None
