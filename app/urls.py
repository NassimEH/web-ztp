from django.urls import path
from app.views import (
    index_views, device_views, help_views, dashboard_views, form_views,
    auth_views
)

app_name = 'app'

urlpatterns = [
    # URLs publiques
    path('', index_views.IndexView.as_view(), name='home'),
    path('help/', help_views.HelpView.as_view(), name='help'),
    
    # URLs protégées
    path('dashboard/', dashboard_views.DashboardView.as_view(), name='dashboard'),
    path('devices/', device_views.DeviceListView.as_view(), name='devices'),
    path('deviceForm/', form_views.AddDeviceView.as_view(), name="device_form"),
    path('templateForm/', form_views.AddTemplateView.as_view(), name="template_form"),
    path('dhcpconfigForm/', form_views.ChangeDHCPConfig.as_view(), name="dhcpconfig_form"),
    path('config/', form_views.ConfFormView.as_view(), name='config'),
    path('deviceCount/', device_views.DeviceCountView.as_view(), name='device_count'),
    
    # URLs d'authentification
    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register_view, name='register'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('profile/', auth_views.profile_view, name='profile'),
    path('profile/change-password/', auth_views.change_password_view, name='change_password'),
] 