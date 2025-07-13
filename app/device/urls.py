from django.urls import path
from .views import (
    DeviceFormView,
    DHCPFormView,
    TemplateFormView,
    DeviceListView,
    DeviceUpdateView,
    DeviceDeleteView,
    TemplateListView,
    TemplateUpdateView,
    TemplateDeleteView,
)

urlpatterns = [
    # Device URLs
    path("device/add/", DeviceFormView.as_view(), name="device_add"),
    path("device/<int:pk>/edit/", DeviceUpdateView.as_view(), name="device_update"),
    path("device/<int:pk>/delete/", DeviceDeleteView.as_view(), name="device_delete"),
    path("devices/", DeviceListView.as_view(), name="device_list"),
    # Template URLs
    path("template/", TemplateListView.as_view(), name="template_list"),
    path("template/add/", TemplateFormView.as_view(), name="template_add"),
    path(
        "template/<int:pk>/edit/", TemplateUpdateView.as_view(), name="template_update"
    ),
    path(
        "template/<int:pk>/delete/",
        TemplateDeleteView.as_view(),
        name="template_delete",
    ),
    # DHCP URLs
    path("dhcp/update/", DHCPFormView.as_view(), name="dhcp_config_update"),
    # Validation URLs
    path("device/add/validate/", DeviceFormView.as_view(), name="device_add_validate"),
    path(
        "device/<int:pk>/edit/validate/",
        DeviceUpdateView.as_view(),
        name="device_update_validate",
    ),
]
