"""
URL configuration for webZtp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from app.views import (
    index_views,
    device_views,
    help_views,
    dashboard_views,
    form_views,
    TermsView,
    PrivacyView,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_views.IndexView.as_view(), name="home"),
    path("dashboard/", dashboard_views.DashboardView.as_view(), name="dashboard"),
    path("devices/", device_views.DeviceListView.as_view(), name="devices"),
    path("deviceForm/", form_views.AddDeviceView.as_view(), name="device_form"),
    path("templateForm/", form_views.AddTemplateView.as_view(), name="template_form"),
    path(
        "dhcpconfigForm/", form_views.ChangeDHCPConfig.as_view(), name="dhcpconfig_form"
    ),
    path("config/", form_views.ConfFormView.as_view(), name="config"),
    path("help/", help_views.HelpView.as_view(), name="help"),
    path("deviceCount/", device_views.DeviceCountView.as_view(), name="device_count"),
    path("terms/", TermsView.as_view(), name="terms"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
    path("auth/", include("app.urls", namespace="auth")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
