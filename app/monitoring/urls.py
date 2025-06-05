from monitoring.views import healthcheck_views
from django.urls import path

urlpatterns = [
    path("status/", healthcheck_views.WebStatusView.as_view(), name="status"),
]
