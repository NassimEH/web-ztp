from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from device.models import Device, Template, DHCPConfig
from device.forms import DeviceForm, TemplateForm


class DeviceModelTest(TestCase):
    """Tests essentiels pour le modèle Device"""

    def test_device_creation(self):
        """Test la création d'un device"""
        device = Device.objects.create(
            serial_number="TEST123", hostname="test-device", ip="192.168.1.100"
        )

        self.assertEqual(device.serial_number, "TEST123")
        self.assertEqual(device.hostname, "test-device")
        self.assertFalse(device.configured)

    def test_device_with_template(self):
        """Test device avec template"""
        template = Template.objects.create(name="Test Template")
        device = Device.objects.create(
            serial_number="TEST123", hostname="test-device", template=template
        )

        self.assertEqual(device.template, template)


class TemplateModelTest(TestCase):
    """Tests essentiels pour le modèle Template"""

    def test_template_creation(self):
        """Test la création d'un template"""
        template = Template.objects.create(name="Test Template")

        self.assertEqual(template.name, "Test Template")
        self.assertEqual(template.variables, [])


class DeviceViewsTest(TestCase):
    """Tests essentiels pour les vues device"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.template = Template.objects.create(name="Test Template")

    def test_device_list_requires_login(self):
        """Test que la liste des devices nécessite une connexion"""
        response = self.client.get(reverse("device_list"))
        self.assertRedirects(response, "/login/?next=/devices/")

    def test_device_list_works_when_logged_in(self):
        """Test la liste des devices"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("device_list"))
        self.assertEqual(response.status_code, 200)

    def test_device_add_form(self):
        """Test le formulaire d'ajout de device"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("device_add"))
        self.assertEqual(response.status_code, 200)

        # Test POST
        data = {
            "serial_number": "TEST123",
            "hostname": "test-device",
            "ip": "192.168.1.100",
            "template": self.template.id,
        }
        response = self.client.post(reverse("device_add"), data)
        # Après un POST réussi, on peut avoir une redirection
        self.assertIn(response.status_code, [200, 302])

        # Vérifier que le device a été créé
        self.assertTrue(Device.objects.filter(serial_number="TEST123").exists())


class DeviceFormTest(TestCase):
    """Tests essentiels pour les formulaires device"""

    def test_device_form_valid(self):
        """Test formulaire device valide"""
        template = Template.objects.create(name="Test Template")
        form_data = {
            "serial_number": "TEST123",
            "hostname": "test-device",
            "ip": "192.168.1.100",
            "template": template.id,
        }
        form = DeviceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_device_form_invalid(self):
        """Test formulaire device invalide"""
        form_data = {
            "serial_number": "",  # Champ requis vide
            "hostname": "test-device",
        }
        form = DeviceForm(data=form_data)
        self.assertFalse(form.is_valid())
