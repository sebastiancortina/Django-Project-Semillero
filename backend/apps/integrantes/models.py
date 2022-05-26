from django.db import models

# Create your models here.
class Integrante(models.Model):
    n_identificacion = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_de_documento =  models.IntegerField(null=False, blank=False, choices=[(1, 'CC'), (2, 'CE'), (3, 'TI'), (4, 'NIT')])
    programa_academico = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    celular = models.BigIntegerField()
    eval = models.TextField()

    def __str__(self):
        return str(self.n_identificacion)

class Lider(models.Model):
    n_identificacion = models.OneToOneField( Integrante, on_delete=models.CASCADE, null=False, blank=True)
    fecha = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    caso_emergencia = models.CharField(max_length=100)
    celular_emergencia = models.BigIntegerField()
    semestre = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.n_identificacion)
