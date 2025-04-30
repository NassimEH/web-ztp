from django import forms


class AddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "input-box", "placeholder": field.label}
            )


class UpdateForm(forms.ModelForm):
    class Meta:
        model = None  # Doit être redéfini dans les sous-classes
        fields = []

    def __init__(self, *args, **kwargs):
        # Préremplir automatiquement avec la première instance existante
        if "instance" not in kwargs:
            instance = self._meta.model.objects.first()
            if instance:
                kwargs["instance"] = instance
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "input-box", "placeholder": field.label}
            )

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
