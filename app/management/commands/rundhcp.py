from django.core.management.base import BaseCommand, CommandError
from ...utils import device_utils, dhcp_utils
from dhcp_server import dhcp_server


class Command(BaseCommand):
    help = "Lance un serveur DHCP avec la configuration en base de donéees pour provisioning ztp"

    def handle(self, *args, **options):
        try:
            server = dhcp_server.DHCPServer("0.0.0.0")
            server.run()
        except Exception as e:
            raise CommandError(e)
