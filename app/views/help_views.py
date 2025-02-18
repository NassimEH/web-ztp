from django.shortcuts import render
from django.views import View

class HelpView(View):
    def get(self, request):
        return render(request, "app/help.html")
