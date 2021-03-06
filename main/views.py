from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import *
from .models import *


class ImgCodeCreateView(CreateAPIView):
    queryset = ImageCode.objects.all()
    serializer_class = ImageCreateSerializer


class ImgList(ListAPIView):
    queryset = ImageCode.objects.all()
    serializer_class = ImagelistSerializer
