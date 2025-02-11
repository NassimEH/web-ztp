from django.db import models

class DHCPServerConfig(models.Model):
    server_ip = models.GenericIPAddressField()
    bind_port = models.IntegerField(default=67)

    def __str__(self):
        return f"DHCP Server at {self.server_ip}:{self.bind_port}"
