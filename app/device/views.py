from django.views.generic import FormView
from .forms import DeviceForm


class DeviceFormView(FormView):
    template_name = "device/device_form.html"
    form_class = DeviceForm
