from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import DeviceForm, TemplateForm, DHCPConfigForm
from .models import Device, Template, DHCPConfig


class DeviceFormView(CreateView):
    model = Device
    template_name = "device/device_form.html"
    form_class = DeviceForm
    success_url = reverse_lazy("device_add")


class DHCPFormView(CreateView):
    model = DHCPConfig
    template_name = "device/device_form.html"
    form_class = DHCPConfigForm
    success_url = reverse_lazy("dhcp_config_update")


class TemplateFormView(CreateView):
    model = Template
    template_name = "device/template_form.html"
    form_class = TemplateForm
    success_url = reverse_lazy("template_add")
