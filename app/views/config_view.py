from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from jinja2 import Template
from ../models import Device

def generate_config(request, device_id):
    device = get_object_or_404(Device, device_id=device_id)
    
    template_content = """
    interface GigabitEthernet1
     ip address {{ ip_address }} {{ subnet_mask }}
    !
    hostname {{ hostname }}
    """
    
    template = Template(template_content)
    config_content = template.render(
        hostname=device.hostname,
        ip_address=device.ip_address,
        subnet_mask=device.subnet_mask
    )
    
    response = HttpResponse(config_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={device.hostname}_config.txt'
    return response
