from django.core.management.base import BaseCommand, CommandError

from dhcp_server import dhcp_server
import env.config as cfg

class Command(BaseCommand):
    help = "Starts a DHCP server with the database configuration for ZTP provisioning"

    def handle(self, *args, **options):
        try:
            server = dhcp_server.DHCPServer(cfg.PRIVATE_IP)
            server.run()
        except Exception as e:
            raise CommandError(f"Erreur DHCP: {e}")
