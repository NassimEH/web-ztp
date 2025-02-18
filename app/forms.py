from django import forms
from .models import Device, Template

class DeviceForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
        empty_label="Aucun",
        widget=forms.Select(attrs={"class":"input-box", "placeholder": "Template"})
    )

    class Meta:
        model = Device
        fields = ["serial_number", "ip", "hostname", "template"]
        widgets = {
            "serial_number": forms.TextInput(
                attrs={"class": "input-box", "placeholder": "Serial Number"}
            ),
            "ip": forms.TextInput(attrs={"class": "input-box", "placeholder": "IP"}),
            "hostname": forms.TextInput(
                attrs={"class": "input-box", "placeholder": "Hostname"}
            ),
        }
