# dhcp/management/commands/run_dhcp_server.py
from django.core.management.base import BaseCommand
from dhcp.dhcp_server import DHCPServer

class Command(BaseCommand):
    help = "Lance le serveur DHCP"

    def handle(self, *args, **options):
        self.stdout.write("Lancement du serveur DHCP...")
        server = DHCPServer(ip_address="0.0.0.0")
        server.run()
