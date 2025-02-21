from django.urls import path
from ./views import log_views as views

urlpatterns = [
    path('logs/', views.log_view, name='log_view'),
    path('log_data/', views.log_data, name='log_data'),
]
