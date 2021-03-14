from rest_framework import serializers
from .models import *


class ImageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageCode
        fields = ['image']


class ImagelistSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageCode
        fields = ['image', 'code']