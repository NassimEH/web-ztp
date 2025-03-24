from django.urls import path
from .views import auth_views

app_name = 'auth'  # Ajout du namespace

urlpatterns = [
    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register_view, name='register'),
    path('logout/', auth_views.logout_view, name='logout'),
] 