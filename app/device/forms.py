from django import forms
from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.layout import Layout, Submit, Div, HTML
from crispy_forms.helper import FormHelper
from .models import Device, Template, DHCPConfig


class DeviceForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
    )

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


class DHCPConfigForm(forms.ModelForm):
    class Meta:
        model = DHCPConfig
        fields = ["subnet", "min_ip_pool", "max_ip_pool"]
        widgets = {
            "min_ip_pool": forms.HiddenInput(),
            "max_ip_pool": forms.HiddenInput(),
            "subnet": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "192.168.1"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "dhcp-config-form"

        self.helper.layout = Layout(
            Div(
                Div(
                    HTML("<h3>Configuration DHCP</h3>"),
                    Div("subnet", css_class="mb-3"),
                    Div(
                        HTML('<label class="form-label">Plage d\'IP</label>'),
                        HTML('<div id="ip-range-display" class="mb-2"></div>'),
                        HTML(
                            '<div id="slider-range" class="ip-range-slider mb-3"></div>'
                        ),
                        "min_ip_pool",
                        "max_ip_pool",
                        css_class="mb-3",
                    ),
                    Submit("submit", "Enregistrer", css_class="btn-primary"),
                    css_class="card-body",
                ),
                css_class="card",
            )
        )


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ["name", "file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "name",
            "file",
            Submit("submit", "Enregistrer", css_class="mt-3"),
        )
