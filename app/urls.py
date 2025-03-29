from django.urls import path
from .views.auth_views import login_view, register_view, logout_view, ProfileView

app_name = 'auth'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
] 