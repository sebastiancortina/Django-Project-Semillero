# from xml.parsers.expat import model
# from zipapp import create_archive
from django.db import models
from apps.coordinador.models import Coordinador

# from apps.integrante.models import Integrante
# from phonenumber_field.modelfields import PhoneNumberField


class Semillero(models.Model):
    nombre = models.CharField("NOMBRE DEL SEMILLERO", max_length=250)
    facultad = models.CharField("FACULTAD", max_length=250)
    programa_academico = models.CharField("PROGRMA ACADÉMICO", max_length=250)
    investigacion = models.CharField(
        "GRUPO DE INVESTIGACIÓN AL CUAL ESTÁ VINCULADO EL SEMILLERO", max_length=250
    )
    investigacion_asociado = models.CharField(
        "LÍNEA Y SUBLÍNEA DE INVESTIGACIÓN ASOCIADOS", max_length=250
    )
    tematica = models.CharField("TÉMATICA DE ESTUDIO DEL SEMILLERO", max_length=250)
    justificacion = models.TextField(
        "JUSTIFICACIÓN DEL SEMILLERO DE INVESTIGACIÓN", max_length=2000
    )
    coordinator = models.ForeignKey(
        Coordinador, on_delete=models.CASCADE, related_name="semillerolist"
    )

    def __str__(self):
        return self.nombre
