# api/urls.py
from django.urls import path
from .views import (
    DeviceListCreateView,
    DeviceDetailView,
    DeviceIPsView,
    TemplateListCreateView,
    TemplateDetailView,
    DHCPConfigView,
)

urlpatterns = [
    path('device/', DeviceListCreateView.as_view(), name='device-list'),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('device/ips/', DeviceIPsView.as_view(), name='device-ips'),
    path('template/', TemplateListCreateView.as_view(), name='template-list'),
    path('template/<int:pk>/', TemplateDetailView.as_view(), name='template-detail'),
    path('dhcpconfig/', DHCPConfigView.as_view(), name='dhcpconfig'),
]
