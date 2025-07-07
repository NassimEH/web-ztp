from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from device.models import Device, Template
from utils.device_utils import get_device_count, get_used_ips
from core.models import LogEntry


class LandingPageView(TemplateView):
    template_name = "core/landing_page.html"


class HelpPageView(TemplateView):
    template_name = "core/help.html"


class DashboardView(TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["device_count"] = get_device_count()
        context["configured_devices"] = Device.objects.filter(configured=True).count()
        context["template_count"] = Template.objects.count()
        context["active_devices"] = Device.objects.filter(configured=False).count()
        context["dhcp_leases"] = len(get_used_ips())
        last_device = Device.objects.order_by("-id").first()
        context["last_device"] = last_device
        logs = LogEntry.objects.select_related("user").all()[:8]
        for log in logs:
            log.is_error_log = log.action.startswith("Erreur")
        context["recent_logs"] = logs
        return context


class ConditionalRedirectView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return redirect("landing_page")

class PrivacyPolicyView(TemplateView):
    template_name = "core/privacy.html"

class TermsOfServiceView(TemplateView):
    template_name = "core/terms.html"