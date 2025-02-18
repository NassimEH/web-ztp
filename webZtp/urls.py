"""
URL configuration for webZtp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app.views import index_views, device_views, template_views, config_device_views, help_views

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views.IndexView.as_view()),
    path('device/', device_views.DeviceListView.as_view()),
    path('mesAppareils/', template_views.TemplateListView.as_view()),
    path('configAppareil/', config_device_views.AddDeviceView.as_view(), name="config_device"),
    path('help/', help_views.HelpView.as_view()),
    path('setting/', help_views.HelpView.as_view()),
    path('password/', help_views.HelpView.as_view()),
    path('deviceCount/', device_views.DeviceCountView.as_view())
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL + "conf/", document_root=settings.MEDIA_ROOT / "conf")
