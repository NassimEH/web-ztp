from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from ..models import Device
from .media_utils import get_site_url

def get_devices():
    return Device

def get_device_count():
    return Device.objects.count()


def get_all_device_order_by(order_by: str, order: str):
    """
    order_by : champs par lequel la liste des devices va être ordonée
    order : "" ou "-"
    "" =  asc
    "-" = desc
    """
    return Device.objects.all().order_by(f"{order}{order_by}")


def get_used_ips() -> set:
    return set(Device.objects.values_list("ip", flat=True))


def get_device_by_serial(serial_number):
    try:
        device = Device.objects.get(serial_number=serial_number)
        return device.ip
    except ObjectDoesNotExist:
        return None


def get_template_url(serial_number):
    try:
        device = Device.objects.get(serial_number=serial_number)
        return f"{get_site_url()}{device.template.file.url}"
    except ObjectDoesNotExist:
        return None


def update_device_status(device_id, status: bool) -> None:
    device = Device.objects.get(id=device_id)
    device.configured = status
    device.save()


def add_device(serial_number, ip, hostname) -> None:
    try:
        device, created = Device.objects.get_or_create(
            serial_number=serial_number,
            defaults={
                "ip": ip,
                "hostname": hostname or f"device-{serial_number[:6]}",
                "template": None,
            },
        )

        if not created:
            if device.ip != ip:
                device.ip = ip
            if hostname and device.hostname != hostname:
                device.hostname = hostname
            device.save()
    except IntegrityError:
        pass
