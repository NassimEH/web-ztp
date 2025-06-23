from django import forms
from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.layout import Layout, Submit, HTML, Field
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

        self.fields["serial_number"].widget.attrs["placeholder"] = "FTX1234W0AB"
        self.fields["ip"].widget.attrs["placeholder"] = "192.168.1.1"
        self.fields["hostname"].widget.attrs["placeholder"] = "toto"
        self.fields["subnet_mask"].widget.attrs["placeholder"] = "255.255.255.0"
        self.fields["default_gateway"].widget.attrs["placeholder"] = "192.168.1.254"
        self.fields["login"].widget.attrs["placeholder"] = "Nom d'utilisateur"
        self.fields["password"].widget.attrs["placeholder"] = "Mot de passe"


class DHCPConfigForm(forms.ModelForm):
    class Meta:
        model = DHCPConfig
        fields = ["subnet", "min_ip_pool", "max_ip_pool"]
        widgets = {
            "min_ip_pool": forms.HiddenInput(),
            "max_ip_pool": forms.HiddenInput(),
            "subnet": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '255.255.255.0'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("subnet"),
            HTML("""
                <div class="form-group">
                    <label>Plage d'IP:</label>
                    <input type="text" id="ip-range" readonly 
                           class="form-control-plaintext mb-2">
                    <div id="slider-range-container" style="position: relative;">
                        <div id="slider-range" class="ip-range-slider mt-3 mb-4"></div>
                    </div>
                </div>
            """),
            Field("min_ip_pool", type="hidden"),
            Field("max_ip_pool", type="hidden"),
            Submit("submit", "Enregistrer", css_class="btn-primary mt-3")
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
