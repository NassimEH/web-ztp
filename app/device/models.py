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
    """This model is used to store the DHCP server configuration
    Only one instance of this model should exist in the database (Singleton).

    The save method ensures that only one instance can be created
    and overwritten the previous one.
    """

    subnet = models.GenericIPAddressField()
    min_ip_pool = models.GenericIPAddressField()
    max_ip_pool = models.GenericIPAddressField()

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists() and not self.pk:
            existing = self.__class__.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        return cls.objects.first()
