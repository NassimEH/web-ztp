from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import DeviceForm, TemplateForm, DHCPConfigForm
from .models import Device, Template, DHCPConfig
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class DeviceListView(LoginRequiredMixin, View):
    def get(self, request):
        devices = Device.objects.select_related("template").all()
        return render(request, "device/device_dashboard.html", {"devices": devices})


class DeviceFormView(LoginRequiredMixin, CreateView):
    model = Device
    template_name = "device/device_form.html"
    form_class = DeviceForm
    success_url = reverse_lazy("device_add")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ajouter l'appareil"
        context["action"] = self.request.path
        return context


class DeviceUpdateView(LoginRequiredMixin, UpdateView):
    model = Device
    template_name = "device/device_form.html"
    form_class = DeviceForm
    success_url = reverse_lazy("device_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Modifier l'appareil"
        context["action"] = self.request.path
        return context


class DHCPFormView(LoginRequiredMixin, CreateView):
    model = DHCPConfig
    template_name = "device/dhcp_config_form.html"
    form_class = DHCPConfigForm
    success_url = reverse_lazy("dhcp_config_update")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TemplateFormView(LoginRequiredMixin, CreateView):
    model = Template
    template_name = "device/template_form.html"
    form_class = TemplateForm
    success_url = reverse_lazy("template_add")
