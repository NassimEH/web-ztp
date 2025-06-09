from django.urls import path
from .views import LandingPageView, ConditionalRedirectView

urlpatterns = [
    path("home/", LandingPageView.as_view(), name="landing_page"),
    path("", ConditionalRedirectView.as_view(), name="home"),
]
