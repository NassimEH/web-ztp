from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.layout import Layout, Submit, Div, HTML
from django import forms
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


class DHCPConfigForm(forms.ModelForm):
    class Meta:
        model = DHCPConfig
        fields = {
            "subnet",
            "min_ip_pool",
            "max_ip_pool",
        }
        widgets = {
            "min_ip_pool": forms.HiddenInput(),
            "max_ip_pool": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        initial_min = (
            self.instance.min_ip_pool
            if self.instance and self.instance.min_ip_pool
            else 0
        )
        initial_max = (
            self.instance.max_ip_pool
            if self.instance and self.instance.max_ip_pool
            else 255
        )

        self.helper.layout = Layout(
            Accordion(
                AccordionGroup(
                    "Configuration DHCP",
                    "subnet",
                    Div(
                        HTML(
                            f"""
                        <div class="range-container mb-4">
                            <label class="form-label mb-3">Plage d'adresses IP</label>
                            <div class="range-slider-wrapper">
                                <div class="range-slider">
                                    <input type="range" min="0" max="255" value="{initial_min}" 
                                           class="form-range min-slider" id="minRange">
                                    <input type="range" min="0" max="255" value="{initial_max}" 
                                           class="form-range max-slider" id="maxRange">
                                </div>
                                <div class="range-values d-flex justify-content-between mt-2">
                                    <div class="min-value-container">
                                        <span class="value-label">Min:</span>
                                        <span class="value-badge bg-primary text-white px-2 rounded" id="minValue">{initial_min}</span>
                                    </div>
                                    <div class="max-value-container">
                                        <span class="value-label">Max:</span>
                                        <span class="value-badge bg-primary text-white px-2 rounded" id="maxValue">{initial_max}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        """
                        ),
                        css_class="mb-3",
                    ),
                    "min_ip_pool",
                    "max_ip_pool",
                    css_class="accordion-item",
                ),
            ),
            Submit("submit", "Enregistrer", css_class="btn-primary mt-3"),
            HTML(
                f"""
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    const minSlider = document.getElementById('minRange');
                    const maxSlider = document.getElementById('maxRange');
                    const minValue = document.getElementById('minValue');
                    const maxValue = document.getElementById('maxValue');
                    const minHidden = document.getElementById('id_min_ip_pool');
                    const maxHidden = document.getElementById('id_max_ip_pool');
                    
                    // Initialisation
                    minHidden.value = {initial_min};
                    maxHidden.value = {initial_max};
                    
                    // Fonction pour mettre à jour le style de la piste
                    function updateTrackStyle() {{
                        const min = parseInt(minSlider.value);
                        const max = parseInt(maxSlider.value);
                        const percentageMin = (min / 255) * 100;
                        const percentageMax = (max / 255) * 100;
                        
                        minSlider.style.background = `
                            linear-gradient(
                                to right,
                                #dee2e6 0%,
                                #dee2e6 ${{percentageMin}}%,
                                #0d6efd ${{percentageMin}}%,
                                #0d6efd ${{percentageMax}}%,
                                #dee2e6 ${{percentageMax}}%,
                                #dee2e6 100%
                            )
                        `;
                    }}
                    
                    // Écouteurs d'événements
                    minSlider.addEventListener('input', function() {{
                        if (parseInt(this.value) > parseInt(maxSlider.value)) {{
                            this.value = maxSlider.value;
                        }}
                        minValue.textContent = this.value;
                        minHidden.value = this.value;
                        updateTrackStyle();
                    }});
                    
                    maxSlider.addEventListener('input', function() {{
                        if (parseInt(this.value) < parseInt(minSlider.value)) {{
                            this.value = minSlider.value;
                        }}
                        maxValue.textContent = this.value;
                        maxHidden.value = this.value;
                        updateTrackStyle();
                    }});
                    
                    // Initialiser le style
                    updateTrackStyle();
                }});
            </script>
            <style>
                .range-container {{
                    padding: 1rem;
                    background: #f8f9fa;
                    border-radius: 0.5rem;
                    border: 1px solid #dee2e6;
                }}
                
                .range-slider-wrapper {{
                    position: relative;
                    padding: 1rem 0;
                }}
                
                .range-slider {{
                    position: relative;
                    width: 100%;
                    height: 6px;
                }}
                
                .range-slider input[type="range"] {{
                    position: absolute;
                    width: 100%;
                    pointer-events: none;
                    -webkit-appearance: none;
                    height: 6px;
                    background: transparent;
                    z-index: 2;
                }}
                
                .range-slider input[type="range"]::-webkit-slider-thumb {{
                    pointer-events: all;
                    -webkit-appearance: none;
                    width: 22px;
                    height: 22px;
                    border-radius: 50%;
                    background: #0d6efd;
                    cursor: pointer;
                    border: 2px solid white;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                    transition: transform 0.1s;
                }}
                
                .range-slider input[type="range"]::-webkit-slider-thumb:hover {{
                    transform: scale(1.1);
                }}
                
                .range-values {{
                    font-size: 0.9rem;
                }}
                
                .value-label {{
                    margin-right: 0.5rem;
                    color: #6c757d;
                }}
                
                .value-badge {{
                    font-weight: 500;
                    min-width: 40px;
                    text-align: center;
                    display: inline-block;
                }}
            </style>
            """
            ),
        )

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["min_ip_pool"] = self.data.get("min_ip_pool", 0)
        cleaned_data["max_ip_pool"] = self.data.get("max_ip_pool", 255)
        return cleaned_data


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
