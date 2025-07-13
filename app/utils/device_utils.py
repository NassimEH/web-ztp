from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from device.models import Device
from utils.media_utils import get_internal_url


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
        return device
    except ObjectDoesNotExist:
        return None


def get_template_url(serial_number):
    print(f"Recherche du template pour serial_number: '{serial_number}'")
    try:
        device = Device.objects.get(serial_number=serial_number)
        print(f"Device trouvé: {device}")
        if device.template:
            template_url = f"{get_internal_url()}/device/{device.id}/template/"
            print(f"Template URL généré: {template_url}")
            return template_url
        else:
            print(f"Aucun template assigné au device {serial_number}")
            return None
    except ObjectDoesNotExist:
        print(f"Device avec serial_number '{serial_number}' non trouvé en base")
        return None


def update_device_status(device_id, status: bool) -> None:
    device = Device.objects.get(id=device_id)
    device.configured = status
    device.save()


def create_or_update_device(serial_number, ip, hostname, configured) -> None:
    try:
        device, created = Device.objects.get_or_create(
            serial_number=serial_number,
            defaults={
                "ip": ip,
                "hostname": hostname or f"device-{serial_number[:6]}",
                "template": None,
                "configured": configured,
            },
        )

        if not created:
            device.ip = ip
            if hostname:
                device.hostname = hostname
            device.configured = configured
            device.save()

    except IntegrityError:
        pass
