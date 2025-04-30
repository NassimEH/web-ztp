from django.shortcuts import render
from django.views.generic import TemplateView


def terms_view(request):
    return render(request, "app/terms.html")


class TermsView(TemplateView):
    template_name = "app/terms.html"
