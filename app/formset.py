from django.forms import modelformset_factory
from app.models import Device

ZTPVariableFormSet = modelformset_factory(
    Device, fields=["subnet_mask", "default_gateway", "username", "password"], extra=1
)
