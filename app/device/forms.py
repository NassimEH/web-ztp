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

        submit_text = "Mettre à jour" if self.instance.pk else "Enregistrer"

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
            Submit("submit", submit_text, css_class="mt-3"),
        )

        self.fields["serial_number"].widget.attrs["placeholder"] = "FTX1234W0AB"
        self.fields["ip"].widget.attrs["placeholder"] = "192.168.1.1"
        self.fields["hostname"].widget.attrs["placeholder"] = "toto"
        self.fields["subnet_mask"].widget.attrs["placeholder"] = "255.255.255.0"
        self.fields["default_gateway"].widget.attrs["placeholder"] = "192.168.1.254"
        self.fields["login"].widget.attrs["placeholder"] = "Nom d'utilisateur"
        self.fields["password"].widget.attrs["placeholder"] = "Mot de passe"

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
            "subnet": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "dhcp-config-form"
        self.helper.attrs = {
            "data-subnet": self.instance.subnet if self.instance.pk else "192.168.1"
        }

        self.helper.layout = Layout(
            Accordion(
                AccordionGroup(
                    "Configuration DHCP",
                    "subnet",
                    HTML(
                        """
                        <label for="ip-range">Plage d'IP:</label>
                        <input type="text" id="ip-range" readonly 
                               style="border:0; color:#f6931f; font-weight:bold;" 
                               class="form-control-plaintext">
                        <div id="slider-range" class="ip-range-slider mt-3 mb-3"></div>
                    """
                    ),
                    "min_ip_pool",
                    "max_ip_pool",
                    css_class="accordion-item",
                )
            ),
            Submit("submit", "Enregistrer", css_class="btn-primary mt-3"),
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
