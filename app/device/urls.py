from django.urls import path
from .views import DeviceFormView

urlpatterns = [
    path("device/add/", DeviceFormView.as_view(), name="device_add"),
]
