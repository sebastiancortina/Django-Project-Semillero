from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Docente(models.Model):
    n_identificacion = models.CharField(max_length=100, primary_key=True)
    lugar_expedicion = models.CharField(max_length=100)
    lugar_nacimiento = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    f_nacimiento = models.CharField(max_length=100)
    direcccion = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    celular = PhoneNumberField(null=False, blank=False)
    c_emergencia = models.CharField(max_length=100)
    n_emergencia = PhoneNumberField(null=False, blank=False)

    def __str__(self):
        return self.n_identificacion


class Semillero(models.Model):
    nombre = models.CharField(max_length=250)
    facultad = models.CharField(max_length=250)
    programa_academico = models.CharField(max_length=250)
    investigacion = models.CharField(max_length=250)
    investigacion_asociado = models.CharField(max_length=250)
    tematica = models.CharField(max_length=250)
    justificacion = models.TextField(max_length=2000)
    coordinador = models.OneToOneField(
        Docente, on_delete=models.CASCADE, null=False, blank=True
    )

    def __str__(self):
        return self.nombre


"""
class idioma(models.Model):
    lengua = models.CharField(max_length=100)
    nivel = models.IntegerField(null=False, blank=False, choices=[(1, 'BÁSICO'), (2, 'INTERMEDIO'), (3, 'AVANZADO')])

    def __str__(self):
        return self.lengua


class informacion_a(models.Model):
    programa_academico = models.CharField(max_length=100)
    informacion = models.CharField(max_length=200)

class curso_i(models.Model):
    tematica = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    horas = models.CharField(max_length=200)
    fecha =  models.CharField(max_length=200)

class experiencia_i(models.Model):
    cvLac = models.BooleanField()

class proyecto_i(models.Model):
"""
