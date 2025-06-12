from django.urls import path
from .views import DeviceFormView, DHCPFormView, TemplateFormView, DeviceListView

urlpatterns = [
    path("device/add/", DeviceFormView.as_view(), name="device_add"),
    path("dhcp/update/", DHCPFormView.as_view(), name="dhcp_config_update"),
    path("template/add/", TemplateFormView.as_view(), name="template_add"),
    path("devices/", DeviceListView.as_view(), name="device_list"),
]
