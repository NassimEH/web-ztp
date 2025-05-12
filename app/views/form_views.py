from app.forms import DeviceForm, TemplateForm, DHCPConfigUpdateForm
from app.formset import ZTPVariableFormSet
from app.utils.view_utils import AddView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect


# class AddDeviceView(AddView):
#     template_name = "app/deviceForm.html"
#     form_class = DeviceForm


class AddDeviceViewZTP(AddView):
    template_name = "app/deviceForm.html"
    form_class = DeviceForm
    formset_class = ZTPVariableFormSet


class AddTemplateView(AddView):
    template_name = "app/templateForm.html"
    form_class = TemplateForm


class ChangeDHCPConfig(AddView):
    template_name = "app/dhcpconfigForm.html"
    form_class = DHCPConfigUpdateForm


@method_decorator(login_required, name="dispatch")
class ConfFormView(FormView):
    def dispatch(self, request, *args, **kwargs):
        form_type = request.POST.get("form_type")
        if form_type == "template":
            self.template_name = "app/templateForm.html"
            self.form_class = TemplateForm
        elif form_type == "dhcp":
            self.template_name = "app/dhcpconfigForm.html"
            self.form_class = DHCPConfigUpdateForm
        else:
            self.template_name = "app/deviceForm.html"
            self.form_class = DeviceForm
        return super().dispatch(request, *args, **kwargs)
