# front/views.py
from django.shortcuts import render

def index(request):
    return render(request, "front/index.html")

def form_view(request):
    return render(request, "front/form.html")

def landing(request):
    return render(request, "front/landing.html")
