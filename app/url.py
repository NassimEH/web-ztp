from django.urls import path
from .views import log_views as views
from .views import auth_views as auth_views

urlpatterns = [
    path("logs/", views.log_view, name="log_view"),
    path("log_data/", views.log_data, name="log_data"),
    path("login/", auth_views.login_view, name="login"),
    path("register/", auth_views.register_view, name="register"),
    path("logout/", auth_views.logout_view, name="logout"),
]
