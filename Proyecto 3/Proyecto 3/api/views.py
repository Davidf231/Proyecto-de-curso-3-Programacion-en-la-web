from django.shortcuts import render
from .models import Shinigami
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import ShinigamiSerializer

class ShinigamiViewSet(viewsets.ModelViewSet):
    queryset=Shinigami.objects.all().order_by('edad')
    serializer_class=ShinigamiSerializer