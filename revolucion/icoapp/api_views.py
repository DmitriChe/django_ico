from .models import Ico
from .serializers import IcoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .permissions import ReadOnly
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication


class IcoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAdminUser|ReadOnly]  # права читать всем, а админу править
    permission_classes = [IsAdminUser]  # права только у админа, простым смертным даже смотреть нельзя
    queryset = Ico.objects.all()
    serializer_class = IcoSerializer
