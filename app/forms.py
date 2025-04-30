from app.models import Device, Template, DHCPConfig
from app.utils.form_utils import AddForm, UpdateForm
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DeviceForm(AddForm):
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
        empty_label="Aucun",
        widget=forms.Select(attrs={"class": "input-box", "placeholder": "Template"}),
    )

    class Meta:
        model = Device
        fields = ["serial_number", "ip", "hostname", "template"]


class TemplateForm(AddForm):
    file = forms.FileField()

    class Meta:
        model = Template
        fields = ["name", "file"]


class DHCPConfigUpdateForm(UpdateForm):
    class Meta:
        model = DHCPConfig
        fields = ["subnet", "min_ip_pool", "max_ip_pool"]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
