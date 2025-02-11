# front/urls.py
from django.urls import path
from .views import index, form_view, landing

urlpatterns = [
    path('', index, name='home'),
    path('form/', form_view, name='form'),
    path('landing/', landing, name='landing'),
]
