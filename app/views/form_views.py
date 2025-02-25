from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template.loader import render_to_string
from app.forms import DeviceForm, TemplateForm, DHCPConfigUpdateForm


class AddView(FormView):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def form_valid(self, form):
        modele = form.save()
        html = render_to_string(
            "app/components/formResponse.html",
            {
                "success": True,
                "modele": modele,
            },
        )

        return HttpResponse(html, status=200)

    def form_invalid(self, form):
        html = render_to_string(
            "app/components/formResponse.html",
            {
                "success": False,
                "form": form,
            },
        )

        return HttpResponse(html, status=200)


class AddDeviceView(AddView):
    template_name = "app/deviceForm.html"
    form_class = DeviceForm


class AddTemplateView(AddView):
    template_name = "app/templateForm.html"
    form_class = TemplateForm


class ChangeDHCPConfig(AddView):
    template_name = "app/dhcpconfigForm.html"
    form_class = DHCPConfigUpdateForm


class ConfFormView(FormView):
   def dispatch(self, request, *args, **kwargs):
        form_type = request.POST.get('form_type')
        if form_type == 'template':
            self.template_name = "app/templateForm.html"
            self.form_class = TemplateForm
        elif form_type == 'dhcp':
            self.template_name = "app/dhcpconfigForm.html"
            self.form_class = DHCPConfigUpdateForm
        else:
            self.template_name = "app/deviceForm.html"
            self.form_class = DeviceForm
        return super().dispatch(request, *args, **kwargs)
