from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class HelpView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "app/help.html")
