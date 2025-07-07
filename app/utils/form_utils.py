"""Not usefull"""

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Field


class AddForm(forms.ModelForm):
    class Meta:
        model = None  # Must be redefined in subclasses
        fields = []
        group = []  # Fields to be grouped together in a Fieldset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-2"
        self.helper.field_class = "col-lg-8"
        self.helper.form_tag = (
            False  # To allow more control over the form tag attributes
        )

        # Adding placeholders and classes to fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )

        # Creating the layout with fields
        layout_fields = []
        regular_fields = []
        grouped_fields = []

        # Separation of fields into regular and grouped
        if hasattr(self.Meta, "group") and self.Meta.group:
            for field_name, field in self.fields.items():
                if field_name in self.Meta.group:
                    grouped_fields.append(field_name)
                else:
                    regular_fields.append(field_name)
        else:
            regular_fields = list(self.fields.keys())

        # Adding regular fields to the layout
        for field_name in regular_fields:
            layout_fields.append(Field(field_name, css_class="field-item"))

        # If we have grouped fields, create a Fieldset with these fields
        if grouped_fields:
            group_fieldset = Fieldset(
                "Configuration avancée",
                *[
                    Field(field_name, css_class="group-field-item")
                    for field_name in grouped_fields
                ],
                css_class="grouped-fields",
            )
            layout_fields.append(group_fieldset)

        # Applying the layout
        self.helper.layout = Layout(*layout_fields)
        # The submit button is now handled in genericForm.html


class UpdateForm(forms.ModelForm):
    class Meta:
        model = None  # Must be redefined in subclasses
        fields = []

    def __init__(self, *args, **kwargs):
        # Automatically pre-fill with the first existing instance
        if "instance" not in kwargs:
            instance = self._meta.model.objects.first()
            if instance:
                kwargs["instance"] = instance

        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-2"
        self.helper.field_class = "col-lg-8"
        self.helper.form_tag = (
            False  # To allow more control over the form tag attributes
        )

        # Adding placeholders and classes to fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )

        # Creating the layout with all the fields
        layout_fields = [
            Field(field_name, css_class="field-item") for field_name in self.fields
        ]
        self.helper.layout = Layout(*layout_fields)
        # The submit button is now handled in genericForm.html

    def save(self, commit=True):
        """
        Surcharge de la méthode save pour s'assurer que la première instance existante
        est mise à jour au lieu de créer une nouvelle instance.
        """
        instance = self._meta.model.objects.first()
        if instance:
            for field in self.Meta.fields:
                setattr(instance, field, self.cleaned_data.get(field))
            if commit:
                instance.save()
            return instance
        else:
            return super().save(commit=commit)
