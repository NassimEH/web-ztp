from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models import Device


class DeviceListView(LoginRequiredMixin, View):
    def get(self, request):
        devices = Device.objects.all()
        return render(request, "app/devices.html", {"devices": devices})


class DeviceDetailView(View):
    def get(self, request, pk):
        # device = get_object_or_404(Device, pk=pk)
        # return render(request, "articles/article_detail.html", {"device": device})
        pass


class DeviceCountView(LoginRequiredMixin, View):
    def get(self, request):
        count = Device.objects.count()
        return render(request, "app/device_count.html", {"count": count})
