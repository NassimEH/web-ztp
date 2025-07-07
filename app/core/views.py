from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from device.models import Device, Template
from utils.device_utils import get_device_count, get_used_ips
from core.models import LogEntry
from django.db.models import Count


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
        # Répartition des équipements par template
        context["devices_by_template"] = Template.objects.annotate(nb=Count('devices')).order_by('-nb')
        # Nombre d'équipements orphelins (sans template)
        context["orphan_devices"] = Device.objects.filter(template__isnull=True).count()
        # Notifications systèmes (exemple statique)
        context["system_notifications"] = [
            "Maintenance prévue le 15/07 à 22h.",
            "Pensez à sauvegarder vos configurations."
        ]
        # Logs de configuration d'appareil (pour affichage ou traitement ultérieur)
        context["config_logs"] = LogEntry.objects.filter(action="Configuration d'un appareil").order_by('-timestamp')[:5]
        context["devices_list"] = Device.objects.select_related("template").all()
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