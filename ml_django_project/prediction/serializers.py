from rest_framework import serializers
from .models import *


class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload
        fields = ('id', 'url', 'image',  'prediction', 'chance')
