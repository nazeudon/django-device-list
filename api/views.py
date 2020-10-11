from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import DeviceSerializer
from .models import Device


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def post(self, request, *args, **kwargs):
        image = request.data['image']
        title = request.data['title']
        Device.objects.create(title=title, image=image)
        return HttpResponse({'message': 'New device created'}, status=200)
