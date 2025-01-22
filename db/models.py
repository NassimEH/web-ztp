"""Fichier contenant le modele de données de l'ORM"""

from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint

from db.database import Base


class Template(Base):
    """Modele de donnée pour un template configuration ZTP"""

    __tablename__ = "templates"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    file_path: Mapped[str] = mapped_column(String)

    devices: Mapped[list["Device"]] = relationship("Device", back_populates="template")


class Device(Base):
    """Modele de donnée pour une machine a configurer"""

    __tablename__ = "devices"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    serial_number: Mapped[str] = mapped_column(String, nullable=False)
    ip: Mapped[str] = mapped_column(String, unique=True)
    hostname: Mapped[str] = mapped_column(String, nullable=True)
    interface: Mapped[str] = mapped_column(String, nullable=True)
    template_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("templates.id"), nullable=True
    )

    template: Mapped[Optional[Template]] = relationship(
        "Template", back_populates="devices"
    )

    __table_args__ = (UniqueConstraint("serial_number", "interface"),)

class DHCPConfig(Base):
    """Modele de donnée des configuration DHCP"""

    __tablename__ = "dhcpconfig"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, default=1)
    subnet: Mapped[str] = mapped_column(String, nullable=False)
    min_ip_pool: Mapped[str] = mapped_column(String, nullable=False)
    max_ip_pool: Mapped[str] = mapped_column(String, nullable=False)
