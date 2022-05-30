from apps.semillero_app.models import Semillero
from apps.semillero_app.apis.serializers import SemilleroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view()
def semillero_list(request):

    semillero = Semillero.objects.all()

    # devuelve una colleccion
    serializers = SemilleroSerializer(semillero, many=True)
    
    return Response(serializers.data)

@api_view()
def semillero_detalle(request, id):
    semillero = Semillero.objects.get(id=id)
    serializers = SemilleroSerializer(semillero)

    return Response(serializers.data)