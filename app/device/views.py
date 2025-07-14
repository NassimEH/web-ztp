import os
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponse
from jinja2 import Environment
from .forms import (
    DeviceForm,
    TemplateForm,
    DHCPConfigForm,
    DeviceDeleteForm,
    TemplateDeleteForm,
)
from .models import Device, Template, DHCPConfig
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from core.models import LogEntry


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

    def post(self, request, *args, **kwargs):
        self.object = None

        if "validate" in request.path:
            form = self.form_class(data=request.POST)
            context = self.get_context_data(form=form)
            context["title"] = "Ajouter l'appareil"
            context["action"] = self.request.path.replace("/validate/", "/")
            return self.render_to_response(context)

        is_unpoly_validation = "X-Up-Validate" in request.headers

        if is_unpoly_validation:
            form = self.form_class(data=request.POST)
            context = self.get_context_data(form=form)
            context["title"] = "Ajouter l'appareil"
            context["action"] = self.request.path
            return self.render_to_response(context)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.create(
            user=self.request.user,
            action="Ajout d'un appareil",
            description=f"Appareil ajouté : {self.object.hostname} ({self.object.ip})",
        )
        return response

    def form_invalid(self, form):
        LogEntry.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            action="Erreur ajout appareil",
            description=f"Échec lors de l'ajout d'un appareil. Erreurs : {form.errors.as_text()}",
        )
        return super().form_invalid(form)


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

    def post(self, request, *args, **kwargs):
        self.object = None

        if "validate" in request.path:
            form = self.form_class(data=request.POST, instance=self.get_object())
            context = self.get_context_data(form=form)
            context["title"] = "Modifier l'appareil"
            context["action"] = self.request.path.replace("/validate/", "/")
            return self.render_to_response(context)

        is_unpoly_validation = "X-Up-Validate" in request.headers

        if is_unpoly_validation:
            form = self.form_class(data=request.POST, instance=self.get_object())
            context = self.get_context_data(form=form)
            context["title"] = "Modifier l'appareil"
            context["action"] = self.request.path
            return self.render_to_response(context)

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.create(
            user=self.request.user,
            action="Modification d'un appareil",
            description=f"Appareil modifié : {self.object.hostname} ({self.object.ip})",
        )
        return response


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
    success_url = reverse_lazy("template_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ajouter un Template"
        context["action"] = self.request.path
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.create(
            user=self.request.user,
            action="Ajout d'un template",
            description=f"Template ajouté : {self.object.name}",
        )
        return response

    def form_invalid(self, form):
        LogEntry.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            action="Erreur ajout template",
            description=f"Échec lors de l'ajout d'un template. Erreurs : {form.errors.as_text()}",
        )
        return super().form_invalid(form)


class DeviceDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        form = DeviceDeleteForm(device)
        return render(
            request, "device/device_delete.html", {"form": form, "device": device}
        )

    def post(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        LogEntry.objects.create(
            user=request.user,
            action="Suppression d'un appareil",
            description=f"Appareil supprimé : {device.hostname} ({device.ip})",
        )
        device.delete()

        devices = Device.objects.select_related("template").all()
        return render(
            request, "device/device_table_fragment.html", {"devices": devices}
        )


class TemplateListView(LoginRequiredMixin, View):
    def get(self, request):
        templates = Template.objects.prefetch_related("devices").all()
        return render(
            request, "device/template_dashboard.html", {"templates": templates}
        )


class TemplateUpdateView(LoginRequiredMixin, UpdateView):
    model = Template
    template_name = "device/template_form.html"
    form_class = TemplateForm
    success_url = reverse_lazy("template_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Modifier le template"
        context["action"] = self.request.path
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        LogEntry.objects.create(
            user=self.request.user,
            action="Modification d'un template",
            description=f"Template modifié : {self.object.name}",
        )
        return response


class TemplateDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        template = get_object_or_404(Template, pk=pk)
        form = TemplateDeleteForm(template)
        return render(
            request, "device/template_delete.html", {"form": form, "template": template}
        )

    def post(self, request, pk):
        template = get_object_or_404(Template, pk=pk)
        LogEntry.objects.create(
            user=request.user,
            action="Suppression d'un template",
            description=f"Template supprimé : {template.name}",
        )
        template.delete()

        templates = Template.objects.all()
        return render(
            request, "device/template_table_fragment.html", {"templates": templates}
        )


class DeviceTemplateView(View):
    """Vue pour afficher le template d'un device avec les variables remplacées"""

    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk)

        if not device.template or not device.template.file:
            return HttpResponse(
                "Aucun template associé à cet appareil.",
                content_type="text/plain",
                status=404,
            )

        try:
            device.template.file.seek(0)
            template_content = device.template.file.read().decode("utf-8")

            env = Environment()
            template = env.from_string(template_content)

            rendered_content = template.render(device.template_variables)

            response = HttpResponse(rendered_content, content_type="text/plain")

            original_filename = os.path.basename(device.template.file.name)
            name_without_ext, ext = os.path.splitext(original_filename)
            filename = f"{device.hostname}_{device.template.name}{ext}"
            response["Content-Disposition"] = f'inline; filename="{filename}"'

            LogEntry.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action="Affichage template device",
                description=f"Template affiché pour l'appareil : {device.hostname}",
            )

            return response

        except Exception as e:
            return HttpResponse(
                f"Erreur lors du rendu du template : {str(e)}",
                content_type="text/plain",
                status=500,
            )
