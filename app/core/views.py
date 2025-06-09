from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = "core/landing_page.html"


class ConditionalRedirectView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("account_profile")
        return redirect("landing_page")
