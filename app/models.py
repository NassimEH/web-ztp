from django.db import models
from django.utils import timezone


class Template(models.Model):
    """Modèle de données pour un template de configuration ZTP"""

    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="conf/", null=True)

    def __str__(self):
        return str(self.name)


class Device(models.Model):
    """Modèle de données pour une machine à configurer"""

    serial_number = models.CharField(max_length=255, unique=True)
    ip = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=255, null=True, blank=True)
    configured = models.BooleanField(default=False)
    template = models.ForeignKey(
        Template, on_delete=models.SET_NULL, null=True, related_name="devices"
    )

    def __str__(self):
        return f"{self.hostname} ({self.ip})"


class DHCPConfig(models.Model):
    """Modèle de données pour une configuration DHCP"""

    subnet = models.GenericIPAddressField()
    min_ip_pool = models.GenericIPAddressField()
    max_ip_pool = models.GenericIPAddressField()

    def __str__(self):
        return f"DHCP: {self.subnet}"

class Action(models.Model):
    ACTION_CHOICES = [
        ('add', 'Add'),
        ('delete', 'Delete'),
        ('modify', 'Modify'),
    ]
    
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.get_action_type_display()} on {self.created_at}"
