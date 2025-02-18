from ..models import DHCPConfig

def get_dhcp_config():
    """Récupère les informations du subnet DHCP et du pool d'adresses IP."""
    config = DHCPConfig.objects.first()
    return config