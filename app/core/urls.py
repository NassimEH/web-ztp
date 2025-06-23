from django.urls import path
from .views import LandingPageView, ConditionalRedirectView, HelpPageView

urlpatterns = [
    path("home/", LandingPageView.as_view(), name="landing_page"),
    path("help/", HelpPageView.as_view(), name="help_page"),
    path("", ConditionalRedirectView.as_view(), name="home"),
]
