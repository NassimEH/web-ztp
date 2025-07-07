from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from allauth.account.views import LoginView as AllauthLoginView
from core.models import LogEntry


class CustomLogoutView(LogoutView):
    """
    Custom logout view that allows users to log out via GET, POST, or OPTIONS requests.

    This view extends the default LogoutView to handle GET requests for logging out,
    in addition to the standard POST and OPTIONS methods. Upon logout, the user is
    redirected to the homepage ("/").
    """

    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)


class CustomLoginView(AllauthLoginView):
    def form_invalid(self, form):
        LogEntry.objects.create(
            user=None,
            action="Erreur connexion",
            description=f"Tentative de connexion échouée pour l'identifiant : {form.cleaned_data.get('login', 'inconnu')}"
        )
        return super().form_invalid(form)
