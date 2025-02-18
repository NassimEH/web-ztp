from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.shortcuts import render
from ..forms import DeviceForm


class AddDeviceView(FormView):
    template_name = "app/configAppareil.html"
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
