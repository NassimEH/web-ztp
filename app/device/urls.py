from django.urls import path
from .views import DeviceFormView, DHCPFormView

urlpatterns = [
    path("device/add/", DeviceFormView.as_view(), name="device_add"),
    path("device/dhcp_conf/", DHCPFormView.as_view(), name="dhcp_config_add"),
]
