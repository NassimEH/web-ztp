from django import forms
from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.layout import Layout, Submit, HTML, ButtonHolder
from crispy_forms.helper import FormHelper
from .models import Device, Template, DHCPConfig


class DeviceForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "id_template",
            }
        ),
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
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self._add_template_variable_fields()

        if hasattr(self, "instance") and self.instance.pk:
            validate_url = f"/device/{self.instance.pk}/edit/validate/"
        else:
            validate_url = "/device/add/validate/"

        self.fields["template"].widget.attrs.update(
            {
                "up-validate": "#template-variables-accordion",
                "up-validate-url": validate_url,
            }
        )

        submit_text = "Mettre à jour" if self.instance.pk else "Enregistrer"

        template_fields = self._get_template_variable_field_names()

        if template_fields:
            self.helper.layout = Layout(
                "serial_number",
                "hostname",
                "ip",
                "template",
                HTML('<div id="template-variables-accordion">'),
                Accordion(
                    AccordionGroup(
                        "Variables du template",
                        *template_fields,
                        css_class="accordion-item",
                    ),
                ),
                HTML("</div>"),
                Submit("submit", submit_text, css_class="mt-3"),
            )
        else:
            self.helper.layout = Layout(
                "serial_number",
                "hostname",
                "ip",
                "template",
                HTML('<div id="template-variables-accordion">'),
                HTML(
                    '<p class="text-muted">Sélectionnez un template pour voir les variables</p>'
                ),
                HTML("</div>"),
                Submit("submit", submit_text, css_class="mt-3"),
            )

    def _add_template_variable_fields(self):
        """Dynamically adds fields for template variables"""
        template = None

        if self.instance.pk and self.instance.template:
            template = self.instance.template
        elif "template" in self.data and self.data["template"]:
            try:
                template = Template.objects.get(pk=self.data["template"])
            except Template.DoesNotExist:
                pass

        if template and template.variables:
            for variable in template.variables:
                field_name = f"template_var_{variable}"

                initial_value = ""
                if self.instance.pk and self.instance.template_variables:
                    initial_value = self.instance.template_variables.get(variable, "")

                self.fields[field_name] = forms.CharField(
                    label=variable.replace("_", " ").title(),
                    required=False,
                    initial=initial_value,
                    help_text=f"Variable du template: {variable}",
                    widget=forms.TextInput(
                        attrs={
                            "class": "form-control",
                            "placeholder": f"Valeur pour {variable}",
                        }
                    ),
                )

    def _get_template_variable_field_names(self):
        """Returns list of field names for template variables"""
        field_names = []
        for field_name in self.fields:
            if field_name.startswith("template_var_"):
                field_names.append(field_name)
        return field_names

    def get_template_variables_data(self):
        """Retrieves template variable data from the form"""
        variables_data = {}
        for field_name, value in self.cleaned_data.items():
            if field_name.startswith("template_var_") and value:
                variable_name = field_name.replace("template_var_", "")
                variables_data[variable_name] = value
        return variables_data

    def save(self, commit=True):
        """Saves the device with template variables"""
        device = super().save(commit=False)

        device.template_variables = self.get_template_variables_data()

        if commit:
            device.save()
        return device


class DHCPConfigForm(forms.ModelForm):
    network_base = forms.GenericIPAddressField(
        required=True,
        label="Subnet",
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ),
        help_text="Adresse réseau de base (ex: 192.168.1.0, 10.0.0.0)",
    )

    min_ip_manual = forms.GenericIPAddressField(
        required=False,
        label="IP minimum",
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ),
    )
    max_ip_manual = forms.GenericIPAddressField(
        required=False,
        label="IP maximum",
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ),
    )

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
        labels = {"subnet": "Masque de sous-réseau"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "dhcp-config-form"

        # Récupérer la configuration DHCP existante ou la première disponible
        dhcp_config = None
        if self.instance.pk:
            dhcp_config = self.instance
        else:
            dhcp_config = DHCPConfig.objects.first()

        if dhcp_config:
            self.fields["min_ip_manual"].initial = dhcp_config.min_ip_pool
            self.fields["max_ip_manual"].initial = dhcp_config.max_ip_pool
            self.fields["subnet"].initial = dhcp_config.subnet

            # Mettre à jour les placeholders avec les vraies valeurs
            self.fields["min_ip_manual"].widget.attrs["placeholder"] = dhcp_config.min_ip_pool
            self.fields["max_ip_manual"].widget.attrs["placeholder"] = dhcp_config.max_ip_pool

            if dhcp_config.min_ip_pool:
                ip_parts = dhcp_config.min_ip_pool.split(".")
                if len(ip_parts) == 4:
                    network_base = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0"
                    self.fields["network_base"].initial = network_base
                    self.fields["network_base"].widget.attrs["placeholder"] = network_base

        self.helper.layout = Layout(
            Accordion(
                AccordionGroup(
                    "Configuration DHCP",
                    "network_base",
                    "subnet",
                    HTML(
                        """
                        <div class="manual-ip-inputs">
                            <div class="row">
                                <div class="col-md-6">
                        """
                    ),
                    "min_ip_manual",
                    HTML(
                        """
                                </div>
                                <div class="col-md-6">
                        """
                    ),
                    "max_ip_manual",
                    HTML(
                        """
                                </div>
                            </div>
                            <div class="ip-sync-info">
                                Vous pouvez saisir les IPs manuellement ou utiliser le slider ci-dessous
                            </div>
                        </div>
                        <div class="mt-3">
                            <label for="ip-range-display">Plage d'IP sélectionnée:</label>
                            <input type="text" id="ip-range-display" readonly 
                                   style="border:0; color:#f6931f; font-weight:bold;" 
                                   class="form-control-plaintext">
                        </div>
                        <div id="slider-range" class="ip-range-slider mt-3 mb-3"></div>
                        <div id="subnet-info" class="mt-2"></div>
                        <div class="text-muted small">
                            <i class="fas fa-info-circle"></i> Le slider se synchronise automatiquement avec la saisie manuelle
                        </div>
                        """
                    ),
                    "min_ip_pool",
                    "max_ip_pool",
                    css_class="accordion-item",
                )
            ),
            Submit("submit", "Enregistrer", css_class="btn-primary mt-3"),
        )

    def clean(self):
        cleaned_data = super().clean()

        network_base = cleaned_data.get("network_base")
        min_ip_manual = cleaned_data.get("min_ip_manual")
        max_ip_manual = cleaned_data.get("max_ip_manual")
        subnet = cleaned_data.get("subnet")

        if not network_base:
            self.add_error(
                "network_base",
                "Le champ 'Subnet' est obligatoire et doit être renseigné.",
            )

        if not subnet:
            self.add_error(
                "subnet",
                "Le champ 'Masque de sous-réseau' est obligatoire et doit être renseigné.",
            )

        if subnet:
            cleaned_data["subnet"] = subnet.strip()
        if min_ip_manual:
            cleaned_data["min_ip_pool"] = min_ip_manual
        if max_ip_manual:
            cleaned_data["max_ip_pool"] = max_ip_manual

        if network_base:
            network_parts = network_base.split(".")
            network_prefix = f"{network_parts[0]}.{network_parts[1]}.{network_parts[2]}"

            min_ip = cleaned_data.get("min_ip_pool")
            max_ip = cleaned_data.get("max_ip_pool")

            if min_ip and not min_ip.startswith(network_prefix):
                self.add_error(
                    "min_ip_manual",
                    f"L'IP minimum doit être dans le réseau {network_prefix}.x",
                )

            if max_ip and not max_ip.startswith(network_prefix):
                self.add_error(
                    "max_ip_manual",
                    f"L'IP maximum doit être dans le réseau {network_prefix}.x",
                )

        return cleaned_data


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
