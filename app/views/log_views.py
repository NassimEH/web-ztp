# from django.shortcuts import render, HttpResponse
# from django.core import serializers
# from .models import Action
# import json

# def log_view(request):
#     actions = Action.objects.all().order_by('-created_at')
#     return render(request, 'log_view.html', {'actions': actions})

# def log_data(request):
#     actions = Action.objects.all().order_by('-created_at')
#     data = serializers.serialize('json', actions)
#     return HttpResponse(data, content_type='application/json')
