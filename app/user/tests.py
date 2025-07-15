from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from user.models import Profile


class ProfileModelTest(TestCase):
    """Tests essentiels pour le modèle Profile"""

    def test_profile_creation_on_user_creation(self):
        """Test que le profil est créé automatiquement avec l'utilisateur"""
        user = User.objects.create_user(username="testuser", password="testpass123")

        # Vérifier que le profile existe
        self.assertTrue(hasattr(user, "profile"))
        self.assertIsInstance(user.profile, Profile)


class UserViewsTest(TestCase):
    """Tests essentiels pour les vues user"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123", email="test@example.com"
        )

    def test_profile_view_requires_login(self):
        """Test que la vue profil nécessite une connexion"""
        response = self.client.get(reverse("account_profile"))
        self.assertRedirects(response, "/login/?next=/me/")

    def test_profile_view_works_when_logged_in(self):
        """Test la vue profil"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("account_profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")
        self.assertIn("device_count", response.context)

    def test_change_password_view(self):
        """Test la vue de changement de mot de passe"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("account_change_password"))
        # La vue redirige vers le profil si ce n'est pas un POST
        self.assertRedirects(response, reverse("account_profile"))

    def test_profile_update(self):
        """Test la mise à jour du profil utilisateur"""
        self.client.login(username="testuser", password="testpass123")

        data = {
            "username": "testuser",  # Inclure le username existant
            "first_name": "Test",
            "last_name": "User",
            "email": "newtest@example.com",
        }
        response = self.client.post(reverse("account_profile"), data)
        self.assertRedirects(response, reverse("account_profile"))

        # Vérifier que les données ont été mises à jour
        user = User.objects.get(username="testuser")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.email, "newtest@example.com")
