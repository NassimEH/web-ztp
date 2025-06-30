from django.urls import path
from .views import LandingPageView, ConditionalRedirectView, HelpPageView, DashboardView, PrivacyPolicyView, TermsOfServiceView

urlpatterns = [
    path("home/", LandingPageView.as_view(), name="landing_page"),
    path("help/", HelpPageView.as_view(), name="help_page"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("", ConditionalRedirectView.as_view(), name="home"),
    path("privacy/", PrivacyPolicyView.as_view(), name="privacy"),
    path("terms/", TermsOfServiceView.as_view(), name="terms"),
]
