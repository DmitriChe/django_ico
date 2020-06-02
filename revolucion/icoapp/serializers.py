from django.conf.urls import url, include
from .models import Ico
from rest_framework import routers, serializers, viewsets


class IcoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ico
        fields = '__all__'
