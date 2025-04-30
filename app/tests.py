from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

# Create your tests here.


class MenuTests(TestCase):
    """
    Tests pour les fonctionnalités du menu latéral
    """

    def setUp(self):
        """Initialisation des tests"""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_menu_visibility_when_logged_in(self):
        """Test si le menu est visible pour un utilisateur connecté"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "navigation")
        self.assertContains(response, "Accueil")
        self.assertContains(response, "Mes appareils")
        self.assertContains(response, "Configurer un appareil")
        self.assertContains(response, "Aide")
        self.assertContains(response, "Profil")
        self.assertContains(response, "Se déconnecter")

    def test_menu_visibility_when_logged_out(self):
        """Test si le menu est visible pour un utilisateur non connecté"""
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "navigation")
        self.assertContains(response, "Accueil")
        self.assertContains(response, "Mes appareils")
        self.assertContains(response, "Configurer un appareil")
        self.assertContains(response, "Aide")
        self.assertContains(response, "Se connecter")
        self.assertContains(response, "S'inscrire")

    def test_menu_responsive_toggle(self):
        """Test si le menu se replie correctement"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "navigation")
        self.assertContains(response, "toggle")
        self.assertContains(response, "active")


class ThemeTests(TestCase):
    """
    Tests pour les fonctionnalités de thème
    """

    def setUp(self):
        """Initialisation des tests"""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_theme_toggle_button_exists(self):
        """Test si le bouton de changement de thème est présent"""
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "theme-toggle")
        self.assertContains(response, "moon-outline")

    def test_theme_storage(self):
        """Test si le thème est correctement stocké dans le localStorage"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "localStorage.setItem('theme'")
        self.assertContains(response, "localStorage.getItem('theme'")

    def test_theme_initial_state(self):
        """Test l'état initial du thème"""
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "prefers-color-scheme")
        self.assertContains(response, "dark")

    def test_theme_switch_functionality(self):
        """Test la fonctionnalité de changement de thème"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "document.body.classList.toggle('dark'")
        self.assertContains(response, "updateThemeIcon")


class ResponsiveTests(TestCase):
    """
    Tests pour les fonctionnalités responsives
    """

    def setUp(self):
        """Initialisation des tests"""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_menu_collapse_functionality(self):
        """Test si le menu se replie correctement en mode responsive"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "navigation.classList.toggle('active'")
        self.assertContains(response, "main.classList.toggle('active'")

    def test_menu_icons_visibility(self):
        """Test si les icônes restent visibles en mode replié"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, "ion-icon")
        self.assertContains(response, "tooltip")

    def test_menu_titles_hidden_when_collapsed(self):
        """Test si les titres sont masqués en mode replié"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("app:dashboard"))
        self.assertContains(response, ".navigation.active .title")
        self.assertContains(response, "display: none !important")
