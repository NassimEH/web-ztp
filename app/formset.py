from django.forms import modelformset_factory, BaseModelFormSet
from app.models import Device
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit, HTML
from crispy_forms.bootstrap import PrependedText, AppendedText
from django.utils.safestring import mark_safe


class BaseZTPVariableFormSet(BaseModelFormSet):
    """
    Base formset for ZTP variables with Crispy Forms integration
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = "formset"
        self.helper.html5_required = True

        # Appliquer des styles à tous les widgets
        for form in self.forms:
            for field_name, field in form.fields.items():
                field.widget.attrs.update(
                    {"class": "form-control", "placeholder": field.label}
                )
                # Customiser les champs spécifiques
                if field_name == "password":
                    field.widget.attrs.update({"autocomplete": "new-password"})

        # Layout amélioré avec des icônes et des descriptions
        self.helper.layout = Layout(
            HTML('<h5 class="mb-3">Variables de configuration ZTP</h5>'),
            Div(
                Div(
                    PrependedText(
                        "subnet_mask",
                        mark_safe('<i class="fas fa-network-wired"></i>'),
                        wrapper_class="col-md-6",
                    ),
                    PrependedText(
                        "default_gateway",
                        mark_safe('<i class="fas fa-route"></i>'),
                        wrapper_class="col-md-6",
                    ),
                    css_class="row mb-3",
                ),
                Div(
                    PrependedText(
                        "username",
                        mark_safe('<i class="fas fa-user"></i>'),
                        wrapper_class="col-md-6",
                    ),
                    PrependedText(
                        "password",
                        mark_safe('<i class="fas fa-key"></i>'),
                        wrapper_class="col-md-6",
                    ),
                    css_class="row mb-3",
                ),
                HTML(
                    '<p class="text-muted small">Ces variables seront utilisées pour remplacer les valeurs dans le fichier de configuration ZTP.</p>'
                ),
                css_class="ztp-variable-group mb-3 p-3 border rounded bg-light",
            ),
        )


ZTPVariableFormSet = modelformset_factory(
    Device,
    fields=["subnet_mask", "default_gateway", "username", "password"],
    formset=BaseZTPVariableFormSet,
    extra=1,
)
