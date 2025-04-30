from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from app.views import (
    index_views, device_views, help_views, dashboard_views, form_views,
    auth_views, privacy_view, terms_view
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
    
    # URLs admin et documentation
    path('admin/', admin.site.urls),
    re_path(r'^docs/(?P<path>.*)$', serve, {
        'document_root': str(settings.BASE_DIR / 'docs/_build/html'),
    }),
    path('privacy/', privacy_view, name='privacy'),
    path('terms/', terms_view, name='terms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 