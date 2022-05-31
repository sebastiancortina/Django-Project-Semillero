from apps.semillero_app.models import Semillero
from apps.semillero_app.apis.serializers import SemilleroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class SemilleroListCUA(APIView):

    def get(self, request):
        semillero = Semillero.objects.all()
        serializers = SemilleroSerializer(semillero, many=True)

        return Response(serializers.data)

    def post(self, request):
        de_serializer = SemilleroSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)


class SemilleroDetalleCUA(APIView):

    def get(self, request, id):
        try:
            semillero = Semillero.objects.get(id=id)
        except Semillero.DoesNotExist:
            return Response({'Error': 'El semillero no existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = SemilleroSerializer(semillero)
        return Response(serializers.data)


    def put(self, request, id):

        try:
            semillero = Semillero.objects.get(id=id)
        except Semillero.DoesNotExist:
            return Response({'Error': 'El semillero no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SemilleroSerializer(semillero, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            semillero = Semillero.objects.get(id=id)
            semillero.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Semillero.DoesNotExist:
            return Response({'Error': 'El semillero no existe'}, status=status.HTTP_404_NOT_FOUND)




















# @api_view(['GET','POST'])
# def semillero_list(request):

#     if request.method == 'GET':
#         # devuelve una colleccion
#         semillero = Semillero.objects.all()
#         serializers = SemilleroSerializer(semillero, many=True)
#         return Response(serializers.data)
    
#     if request.method == 'POST':
#         de_serializer = SemilleroSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def semillero_detalle(request, id):

#     if request.method == 'GET':
#         try:
#             semillero = Semillero.objects.get(id=id)
#             serializers = SemilleroSerializer(semillero)
#             return Response(serializers.data)
#         except Semillero.DoesNotExist:
#             return Response({'Error': 'El semillero no existe'}, status=status.HTTP_404_NOT_FOUND)

      

        
    
#     if request.method == 'PUT':
#         semillero = Semillero.objects.get(id=id)

#         de_serializer = SemilleroSerializer(semillero, data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'DELETE':
#         try:
#             semillero = Semillero.objects.get(id=id)
#             semillero.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Semillero.DoesNotExist:
#             return Response({'Error': 'El semillero no existe'}, status=status.HTTP_404_NOT_FOUND)


        
    
     

   