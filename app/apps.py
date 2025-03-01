from django.apps import AppConfig
from app.models import DHCPConfig

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        # Vérifier si un objet existe déjà
        if not DHCPConfig.objects.exists():
            DHCPConfig.objects.create(
                subnet="192.168.1.0",
                min_ip_pool="192.168.1.100",
                max_ip_pool="192.168.1.200"
            )
