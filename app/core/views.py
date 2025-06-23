from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = "core/landing_page.html"


class HelpPageView(TemplateView):
    template_name = "core/help.html"


class DashboardView(TemplateView):
    template_name = "core/dashboard.html"


class ConditionalRedirectView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return redirect("landing_page")
