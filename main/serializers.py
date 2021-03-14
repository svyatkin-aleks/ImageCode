from rest_framework import serializers
from .models import *


class ImageCreateSerializer(serializers.ModelSerializer):
    cod = serializers.ReadOnlyField(source='article')

    class Meta:
        model = ArticleImage
        fields = ['image', 'cod']