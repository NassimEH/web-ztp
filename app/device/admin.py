from django.contrib import admin
from .models import Device, DHCPConfig, Template

admin.site.register(Device)
admin.site.register(DHCPConfig)
admin.site.register(Template)
