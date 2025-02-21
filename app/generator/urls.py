from django.urls import path
from . import views

urlpatterns = [
    path('generate-config/<str:device_id>/', views.generate_config, name='generate_config'),
]
