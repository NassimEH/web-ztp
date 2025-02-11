# api/models.py
from django.db import models

class Template(models.Model):
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.file_path

class Device(models.Model):
    serial_number = models.CharField(max_length=255)
    ip = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    interface = models.CharField(max_length=255, blank=True, null=True)
    template = models.ForeignKey(Template, related_name="devices", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ("serial_number", "interface")

    def __str__(self):
        return f"{self.serial_number} ({self.ip})"

class DHCPConfig(models.Model):
    subnet = models.GenericIPAddressField()
    min_ip_pool = models.GenericIPAddressField()
    max_ip_pool = models.GenericIPAddressField()

    def __str__(self):
        return f"DHCP Config: {self.subnet}"
