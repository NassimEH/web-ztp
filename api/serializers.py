# api/serializers.py
from rest_framework import serializers
from .models import Device, Template, DHCPConfig

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'file_path']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'serial_number', 'ip', 'hostname', 'interface', 'template']

class DHCPConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DHCPConfig
        fields = ['id', 'subnet', 'min_ip_pool', 'max_ip_pool']
