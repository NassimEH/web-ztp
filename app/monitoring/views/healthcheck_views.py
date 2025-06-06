from django.views import View
from django.http import JsonResponse


class WebStatusView(View):
    def get(self, _request):
        return JsonResponse({"status": "ok"})
