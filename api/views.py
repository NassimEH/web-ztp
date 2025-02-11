# api/views.py
from rest_framework import generics
from .models import Device, Template, DHCPConfig
from .serializers import DeviceSerializer, TemplateSerializer, DHCPConfigSerializer

# Pour créer un Device et lister les devices
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# Pour récupérer un Device par son ID
class DeviceDetailView(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# Pour récupérer uniquement la liste des IPs
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import F

class DeviceIPsView(APIView):
    def get(self, request):
        ips = Device.objects.values_list('ip', flat=True)
        return Response(list(ips))

# Pour la configuration DHCP
class DHCPConfigView(generics.RetrieveUpdateAPIView):
    queryset = DHCPConfig.objects.all()
    serializer_class = DHCPConfigSerializer

# Pour les Templates
class TemplateListCreateView(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class TemplateDetailView(generics.RetrieveAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
