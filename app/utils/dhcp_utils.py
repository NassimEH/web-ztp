from device.models import DHCPConfig


def get_dhcp_config():
    """Retrieves DHCP subnet and IP address pool information."""
    config = DHCPConfig.objects.first()
    return config
