from django.test import TestCase
from device.models import Device, Template
from utils.device_utils import (
    get_all_device_order_by,
    get_used_ips,
    get_device_by_serial,
)
from utils.jinja_utils import extract_jinja_variables


class DeviceUtilsTest(TestCase):
    """Tests essentiels pour les utilitaires device"""

    def setUp(self):
        self.template = Template.objects.create(name="Test Template")
        Device.objects.create(
            serial_number="DEV001",
            hostname="device-1",
            ip="192.168.1.100",
            template=self.template,
        )
        Device.objects.create(
            serial_number="DEV002", hostname="device-2", ip="192.168.1.101"
        )

    def test_get_all_device_order_by(self):
        """Test le tri des devices"""
        devices_asc = get_all_device_order_by("hostname", "")
        devices_desc = get_all_device_order_by("hostname", "-")

        self.assertEqual(len(devices_asc), 2)
        self.assertEqual(len(devices_desc), 2)
        self.assertEqual(devices_asc.first().hostname, "device-1")
        self.assertEqual(devices_desc.first().hostname, "device-2")

    def test_get_used_ips(self):
        """Test la récupération des IPs utilisées"""
        used_ips = get_used_ips()

        self.assertIn("192.168.1.100", used_ips)
        self.assertIn("192.168.1.101", used_ips)
        self.assertEqual(len(used_ips), 2)

    def test_get_device_by_serial(self):
        """Test la récupération d'un device par serial"""
        device = get_device_by_serial("DEV001")
        self.assertIsNotNone(device)
        self.assertEqual(device.hostname, "device-1")

        # Test avec serial inexistant
        device = get_device_by_serial("INEXISTANT")
        self.assertIsNone(device)


class JinjaUtilsTest(TestCase):
    """Tests essentiels pour les utilitaires Jinja"""

    def test_extract_jinja_variables(self):
        """Test l'extraction des variables Jinja"""
        template_content = """
        hostname {{ hostname }}
        ip {{ ip_address }}
        vlan {{ vlan_id }}
        """

        variables = list(extract_jinja_variables(template_content))

        self.assertIn("hostname", variables)
        self.assertIn("ip_address", variables)
        self.assertIn("vlan_id", variables)
        self.assertEqual(len(variables), 3)
