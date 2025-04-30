from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template.loader import render_to_string


class AddView(FormView):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST"])

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
