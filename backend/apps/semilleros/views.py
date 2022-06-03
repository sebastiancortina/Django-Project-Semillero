from rest_framework import viewsets

from rest_framework.response import Response

# from rest_framework import status
from rest_framework import permissions

# models
from .models import Semillero

# serializers
from .serializers import SemilleroSerializer, SemilleroGetSerializer


class SemilleroViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = SemilleroSerializer
    queryset = Semillero.objects.all()

    def list(self, _):
        queryset = Semillero.objects.all()
        serializer = SemilleroGetSerializer(queryset, many=True)
        return Response(serializer.data)
