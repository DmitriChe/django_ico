from .models import Ico
from .serializers import IcoSerializer
from rest_framework import viewsets


class IcoViewSet(viewsets.ModelViewSet):
    queryset = Ico.objects.all()
    serializer_class = IcoSerializer
