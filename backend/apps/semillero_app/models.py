#from xml.parsers.expat import model
from zipapp import create_archive
from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

class Semillero(models.Model):
    nombre = models.CharField('NOMBRE DEL SEMILLERO', max_length=250)
    facultad = models.CharField('FACULTAD', max_length=250)
    programa_academico = models.CharField('PROGRMA ACADÉMICO', max_length=250)
    investigacion = models.CharField('GRUPO DE INVESTIGACIÓN AL CUAL ESTÁ VINCULADO EL SEMILLERO',max_length=250)
    investigacion_asociado = models.CharField('LÍNEA Y SUBLÍNEA DE INVESTIGACIÓN ASOCIADOS', max_length=250)
    tematica = models.CharField('TÉMATICA DE ESTUDIO DEL SEMILLERO', max_length=250)
    justificacion = models.TextField(' JUSTIFICACIÓN DEL SEMILLERO DE INVESTIGACIÓN', max_length=2000)

    def __str__(self):
        return self.nombre   








"""

class Actividad_C_T(models.Model):
    nombre =  models.CharField(max_length=100)
    actividad = models.CharField(max_length=100)
    tipo_de_vinculacion = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Actividad_I(models.Model):
    participacion_c =  models.IntegerField(null=False, blank=False, choices=[(1, 'Si'), (2, 'No')])
    actividad = models.ForeignKey(Actividad_C_T, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return str(self.participacion_c)

class Resultado_D_I(models.Model):
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    publicado =  models.CharField(max_length=100)
    año = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    _a = models.CharField(max_length=100)
    año = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Proyecto_De_Investigacion(models.Model):
    participacion_p_i = models.IntegerField(null=False, blank=False, choices=[(1, 'Si'), (2, 'No')])
    proyecto = models.ForeignKey( Proyecto, on_delete=models.CASCADE, null=False, blank=True)
    resultado = models.OneToOneField( Resultado_D_I, on_delete=models.CASCADE, null=False, blank=True)
    actividad = models.OneToOneField( Actividad_I, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return str(self.participacion_p_i)
class Experiencia_En_Investigacion(models.Model):
    cvlac_registrado = models.IntegerField(null=False, blank=False, choices=[(1, 'Si'), (2, 'No')])
    proyecto_i = models.OneToOneField( Proyecto_De_Investigacion, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return str(self.cvlac_registrado)

class Curso(models.Model):
    tematica = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    horas = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)

    def __str__(self):
        return self.tematica

class Informacion_Academica(models.Model):
   programa = models.IntegerField(null=False, blank=False, choices=[(1, 'PREGRADO'), (2, 'POSGRADOS')])
   informacion_p = models.CharField(max_length=100)

   def __str__(self):
        return str(self.programa)

class Idioma(models.Model):
    lengua = models.CharField(max_length=100)
    nivel = models.IntegerField(null=False, blank=False, choices=[(1, 'BÁSICO'), (2, 'INTERMEDIO'), (3, 'AVANZADO')])

    def __str__(self):
        return str(self.lengua)
"""



"""
class Coordinator(models.Model):
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
    idioma = models.ForeignKey( Idioma, on_delete=models.CASCADE, null=False, blank=False)
    informacion_academica = models.ForeignKey( Informacion_Academica, on_delete=models.CASCADE, null=False, blank=False)
    curso =  models.ForeignKey( Curso, on_delete=models.CASCADE, null=False, blank=False)
    experiencia_en_investigacion =  models.OneToOneField( Experiencia_En_Investigacion, on_delete=models.CASCADE, null=False, blank=False)
    coordinador = models.OneToOneField( Semillero, on_delete=models.CASCADE, null=False, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.n_identificacion
"""


