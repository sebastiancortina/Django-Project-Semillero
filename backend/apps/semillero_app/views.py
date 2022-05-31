from django.shortcuts import render
from apps.semillero_app.models import Semillero
from django.http import JsonResponse



"""
# Create your views here.
def semillero_list(request):

    semillero = Semillero.objects.all()
    data = {
        'semillero': list(semillero.values())
    }

    return JsonResponse(data)

def semillero_detalle(request, id):
    semillero = Semillero.objects.get(id=id)

    data = {
            "nombre": semillero.nombre,
            "facultad": semillero.facultad,
            "programa_academico": semillero.programa_academico,
            "investigacion": semillero.investigacion,
            "investigacion_asociado": semillero.investigacion_asociado,
            "tematica": semillero.tematica,
            "justificacion": semillero.justificacion,
        }

    return JsonResponse(data)
"""