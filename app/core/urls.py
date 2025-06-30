from django.urls import path
from .views import LandingPageView, ConditionalRedirectView, HelpPageView, DashboardView

urlpatterns = [
    path("home/", LandingPageView.as_view(), name="landing_page"),
    path("help/", HelpPageView.as_view(), name="help_page"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("", ConditionalRedirectView.as_view(), name="home"),
    path("privacy/", ConditionalRedirectView.as_view(), name="privacy"),
    path("terms/", ConditionalRedirectView.as_view(), name="terms"),
]
