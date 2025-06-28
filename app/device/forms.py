from django import forms
from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.layout import Layout, Submit, HTML, ButtonHolder
from crispy_forms.helper import FormHelper
from .models import Device, Template, DHCPConfig


class DeviceForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
    )

    ip = forms.GenericIPAddressField(
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
            "hostname",
            "ip",
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


class DHCPConfigForm(forms.ModelForm):
    class Meta:
        model = DHCPConfig
        fields = ["subnet", "min_ip_pool", "max_ip_pool"]
        widgets = {
            "min_ip_pool": forms.HiddenInput(),
            "max_ip_pool": forms.HiddenInput(),
            "subnet": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "255.255.255.0"}
            ),
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

        submit_text = "Mettre à jour" if self.instance.pk else "Enregistrer"

        self.helper.layout = Layout(
            "name",
            "file",
            Submit("submit", submit_text, css_class="btn-primary mt-3"),
        )


class DeviceDeleteForm(forms.Form):
    """Formulaire de confirmation de suppression d'un appareil"""

    def __init__(self, device, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device = device
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            HTML(f"<h4>Supprimer l'appareil : {device}</h4>"),
            HTML(
                '<p class="text-muted">Êtes-vous sûr de vouloir supprimer cet appareil ?</p>'
            ),
            ButtonHolder(
                Submit("delete", "Supprimer", css_class="btn-danger"),
                HTML(
                    '<button type="button" class="btn btn-secondary" up-dismiss>Annuler</button>'
                ),
            ),
        )


class TemplateDeleteForm(forms.Form):
    """Formulaire de confirmation de suppression d'un template"""

    def __init__(self, template, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = template
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            HTML(f"<h4>Supprimer le template : {template}</h4>"),
            HTML(
                '<p class="text-muted">Êtes-vous sûr de vouloir supprimer ce template ?</p>'
            ),
            ButtonHolder(
                Submit("delete", "Supprimer", css_class="btn-danger"),
                HTML(
                    '<button type="button" class="btn btn-secondary" up-dismiss>Annuler</button>'
                ),
            ),
        )
