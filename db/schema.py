"""Fichier contenant les schémas Pydantic:
Les schémas Pydantic permetent de gerer le typages
et l'affichage des champs entre l'API et la base de donnée"""

from typing import Optional

from pydantic import BaseModel
from pydantic.networks import IPv4Address


class DeviceSchema(BaseModel):
    """Schéma Pydantic pour un une machine a configurer"""

    serial_number: str
    ip: IPv4Address
    hostname: Optional[str] = None
    interface: Optional[str] = None
    template_id: Optional[int] = None

    class Config:
        from_attributes = True


class TemplateSchema(BaseModel):
    """Schéma Pydantic pour un template configuration ZTP"""

    file_path: str

    class Config:
        from_attributes = True


class DHCPConfigSchema(BaseModel):
    """Schéma Pydantic pour une configuration DHCP"""

    subnet: IPv4Address
    min_ip_pool: Optional[IPv4Address]
    max_ip_pool: Optional[IPv4Address]

    class Config:
        from_attributes = True
