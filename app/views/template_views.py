from django.shortcuts import render, get_object_or_404
from django.views import View
from ..models import Template

class TemplateListView(View):
    def get(self, request):
        templates = Template.objects.all()
        return render(request, "app/mesAppareils.html", {"templates": templates})
