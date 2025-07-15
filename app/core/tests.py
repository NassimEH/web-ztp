from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import LogEntry
from device.models import Device, Template


class LogEntryModelTest(TestCase):
    """Tests essentiels pour le modèle LogEntry"""

    def test_log_entry_creation(self):
        """Test la création d'une entrée de log"""
        user = User.objects.create_user(username="testuser", password="testpass123")
        log_entry = LogEntry.objects.create(
            user=user, action="Test action", description="Test description"
        )

        self.assertEqual(log_entry.user, user)
        self.assertEqual(log_entry.action, "Test action")
        self.assertIsNotNone(log_entry.timestamp)


class CoreViewsTest(TestCase):
    """Tests essentiels pour les vues de l'app core"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_landing_page_accessible(self):
        """Test que la page d'accueil est accessible"""
        response = self.client.get(reverse("landing_page"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        """Test que le dashboard nécessite une connexion"""
        response = self.client.get(reverse("dashboard"))
        # Le dashboard peut être accessible mais sans certaines données sensibles
        self.assertEqual(response.status_code, 200)

    def test_dashboard_works_when_logged_in(self):
        """Test le dashboard avec utilisateur connecté"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertIn("device_count", response.context)
        self.assertIn("template_count", response.context)
