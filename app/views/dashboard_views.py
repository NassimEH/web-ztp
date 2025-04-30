from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):
    login_url = "auth:login"

    def get(self, request):
        return render(request, "app/dashboard.html")
