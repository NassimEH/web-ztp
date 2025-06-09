from django.db import models


class Template(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="conf/", null=True)

    def __str__(self):
        return str(self.name)


class Device(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    ip = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=255, null=True, blank=True)
    configured = models.BooleanField(default=False)
    template = models.ForeignKey(
        Template,
        on_delete=models.SET_NULL,
        null=True,
        related_name="devices",
    )

    subnet_mask = models.CharField(max_length=255, null=True, blank=True)
    default_gateway = models.GenericIPAddressField(null=True, blank=True)
    login = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.hostname} ({self.ip})"


class DHCPConfig(models.Model):
    subnet = models.GenericIPAddressField()
    min_ip_pool = models.GenericIPAddressField()
    max_ip_pool = models.GenericIPAddressField()
