"""Fichier contenant les schémas Pydantic:
Les schémas Pydantic permetent de gerer le typages et l'affichage des champs entre l'API et la base de donnée"""

from pydantic import BaseModel
from pydantic.networks import IPv4Address
from pydantic_extra_types.mac_address import MacAddress

class ClientSchema(BaseModel):
    mac: MacAddress
    ip: IPv4Address
    hostname: str 

    class Config:
        from_attributes = True