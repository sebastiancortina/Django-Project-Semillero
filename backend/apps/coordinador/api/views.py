from apps.coordinador.models import Coordinador
from apps.coordinador.api.serializers import CoordinadorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class SemilleroListCUA(APIView):
  
    def get(self, request):
        coordinador = Coordinador.objects.all()
        serializers = CoordinadorSerializer(coordinador, many=True)

        return Response(serializers.data)

    def post(self, request):
        de_serializer = CoordinadorSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)


class SemilleroDetalleCUA(APIView):

    def get(self, request, id):
        try:
            coordinador = Coordinador.objects.get(id=id)
        except Coordinador.DoesNotExist:
            return Response({'Error': 'El coordinador no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = CoordinadorSerializer(coordinador)
        return Response(serializers.data)


    def put(self, request, id):

        try:
            coordinador = Coordinador.objects.get(id=id)
        except Coordinador.DoesNotExist:
            return Response({'Error': 'El coordinador no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CoordinadorSerializer(coordinador, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            coordinador = Coordinador.objects.get(id=id)
            coordinador.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Coordinador.DoesNotExist:
            return Response({'Error': 'El coordinador no existe'}, status=status.HTTP_404_NOT_FOUND)