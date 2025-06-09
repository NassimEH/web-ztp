from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.layout import Layout, Submit
from django import forms
from crispy_forms.helper import FormHelper
from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            "serial_number",
            "ip",
            "hostname",
            "template",
            "subnet_mask",
            "default_gateway",
            "login",
            "password",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "serial_number",
            "ip",
            "hostname",
            "template",
            Accordion(
                AccordionGroup(
                    "Champs de configuration ZTP",
                    "subnet_mask",
                    "default_gateway",
                    "login",
                    "password",
                    css_class="accordion-item",
                ),
            ),
            Submit("submit", "Enregistrer", css_class="mt-3"),
        )
