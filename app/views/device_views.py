from django.shortcuts import render
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
        return HttpResponse(
            f"""
            <br>
            <div class="errorHandling">
                <p style='color: green;'>✅ Appareil ajouté : {device.hostname} ({device.ip})</p>
            </div>
            """,
            status=200,
        )

    def form_invalid(self, form):
        errors_html = "<ul>"
        for field, errors in form.errors.items():
            for error in errors:
                errors_html += f"<li>{field}: {error}</li>"
        errors_html += "</ul>"

        return HttpResponse(
            f"""
            <br>
            <div class="errorHandling">
                <p style="color: red;">❌ Erreur :</p>
                {errors_html}
            </div>
            """,
            status=200,
        )
