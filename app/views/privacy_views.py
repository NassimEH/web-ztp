from django.shortcuts import render
from django.views.generic import TemplateView

def privacy_view(request):
    return render(request, 'app/privacy.html')

class PrivacyView(TemplateView):
    template_name = 'app/privacy.html' 