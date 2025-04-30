from django.views.generic import TemplateView
from django.shortcuts import render

def privacy_view(request):

 

    return render(request, 'app/privacy.html')
 


 

def terms_view(request):
 

    return render(request, 'app/terms.html')

class TermsView(TemplateView):
    template_name = 'app/terms.html'

class PrivacyView(TemplateView):
    template_name = 'app/privacy.html'
