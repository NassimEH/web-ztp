from django import template
from app.utils import device_utils


register = template.Library()


@register.simple_tag(takes_context=True)
def device_count(context):
    return device_utils.get_device_count()


@register.inclusion_tag("app/components/card.html")
def render_card(title, value, icon):
    return {"title": title, "value": value, "icon": icon}


@register.inclusion_tag("app/components/deviceRows.html")
def render_device_rows(order_by="hostname", order=""):
    devices = device_utils.get_all_device_order_by(order_by, order)
    return { "devices" : devices }
