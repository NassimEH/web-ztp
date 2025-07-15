from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from device.models import Device, Template
from core.models import LogEntry
from django.db.models import Count, Case, When, IntegerField


class LandingPageView(TemplateView):
    template_name = "core/landing_page.html"


class HelpPageView(TemplateView):
    template_name = "core/help.html"


class DashboardView(TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Une seule requête pour toutes les statistiques des devices
        device_stats = Device.objects.aggregate(
            total_count=Count("id"),
            configured_count=Count(
                Case(When(configured=True, then=1), output_field=IntegerField())
            ),
            orphan_count=Count(
                Case(When(template__isnull=True, then=1), output_field=IntegerField())
            ),
        )

        context["device_count"] = device_stats["total_count"]
        context["configured_devices"] = device_stats["configured_count"]
        context["orphan_devices"] = device_stats["orphan_count"]

        # Autres requêtes nécessaires
        context["template_count"] = Template.objects.count()
        context["last_device"] = Device.objects.order_by("-id").first()

        # Logs récents avec optimisation
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
