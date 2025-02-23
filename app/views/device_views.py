from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views import View
from django.views.generic.edit import FormView
from django.http import HttpResponse

from app.forms import DeviceForm
from app.models import Device


class DeviceListView(View):
    def get(self, request):
        return render(request, "app/devices.html")


class DeviceDetailView(View):
    def get(self, request, pk):
        # device = get_object_or_404(Device, pk=pk)
        # return render(request, "articles/article_detail.html", {"device": device})
        pass


class DeviceCountView(View):
    def get(self, request):
        device_count = Device.objects.count()
        return JsonResponse({"device_count": device_count})


class AddDeviceView(FormView):
    template_name = "app/deviceForm.html"
    form_class = DeviceForm

    def form_valid(self, form):
        device = form.save()
        html = render_to_string(
            "app/components/formResponse.html",
            {
                "success": True,
                "modele": device,
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
