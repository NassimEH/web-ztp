from app.models import Device, Template, DHCPConfig
from app.utils.form_utils import AddForm, UpdateForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Field, HTML
from crispy_forms.bootstrap import TabHolder, Tab, FormActions, PrependedText
from django.utils.safestring import mark_safe


class DeviceForm(AddForm):
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
        empty_label="Aucun",
    )

    class Meta:
        model = Device
        fields = ["serial_number", "ip", "hostname", "template"]

        group = [
            "subnet_mask",
            "default_gateway",
            "username",
            "password",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = "device-form"
        self.helper.layout = Layout(
            Fieldset(
                "Informations principales",
                PrependedText(
                    "serial_number", mark_safe('<i class="fas fa-barcode"></i>')
                ),
                PrependedText("ip", mark_safe('<i class="fas fa-network-wired"></i>')),
                PrependedText("hostname", mark_safe('<i class="fas fa-server"></i>')),
                PrependedText(
                    "template", mark_safe('<i class="fas fa-file-code"></i>')
                ),
            ),
            Fieldset(
                "Configuration avancée",
                Div(
                    Div(
                        PrependedText(
                            "subnet_mask", mark_safe('<i class="fas fa-sitemap"></i>')
                        ),
                        css_class="col-md-6",
                    ),
                    Div(
                        PrependedText(
                            "default_gateway", mark_safe('<i class="fas fa-route"></i>')
                        ),
                        css_class="col-md-6",
                    ),
                    css_class="row",
                ),
                Div(
                    Div(
                        PrependedText(
                            "username", mark_safe('<i class="fas fa-user"></i>')
                        ),
                        css_class="col-md-6",
                    ),
                    Div(
                        PrependedText(
                            "password", mark_safe('<i class="fas fa-key"></i>')
                        ),
                        css_class="col-md-6",
                    ),
                    css_class="row",
                ),
                css_class="border-top pt-3 mt-3",
            ),
        )


class TemplateForm(AddForm):
    file = forms.FileField()

    class Meta:
        model = Template
        fields = ["name", "file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = "template-form"
        self.helper.layout = Layout(Field("name"), Field("file"))


class DHCPConfigUpdateForm(UpdateForm):
    class Meta:
        model = DHCPConfig
        fields = ["subnet", "min_ip_pool", "max_ip_pool"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = "dhcp-config-form"
        self.helper.layout = Layout(
            Field("subnet"),
            Div(
                Div(Field("min_ip_pool"), css_class="col-md-6"),
                Div(Field("max_ip_pool"), css_class="col-md-6"),
                css_class="row",
            ),
        )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-2"
        self.helper.field_class = "col-lg-8"
        self.helper.form_method = "post"

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

        self.helper.layout = Layout(
            Fieldset(
                "Créer un nouveau compte",
                PrependedText(
                    "username",
                    mark_safe('<i class="fas fa-user"></i>'),
                    css_class="input-box",
                ),
                PrependedText(
                    "email",
                    mark_safe('<i class="fas fa-envelope"></i>'),
                    css_class="input-box",
                ),
                PrependedText(
                    "password1",
                    mark_safe('<i class="fas fa-lock"></i>'),
                    css_class="input-box",
                ),
                PrependedText(
                    "password2",
                    mark_safe('<i class="fas fa-lock"></i>'),
                    css_class="input-box",
                ),
            )
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
