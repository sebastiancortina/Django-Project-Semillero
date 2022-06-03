from django.db import models


class Coordinador(models.Model):
    n_identificacion = models.BigIntegerField(
        "NÚMERO DE IDENTIFICACIÓN", primary_key=True
    )
    nombre = models.CharField("NOMBRE COMPLETO", max_length=250)
    f_nacimiento = models.CharField("FECHA DE NACIMIENTO", max_length=100)
    lugar_expedicion = models.CharField("LUGAR DE EXPEDICIÓN ID", max_length=100)
    lugar_nacimiento = models.CharField("LUGAR DE NACIMIENTO", max_length=100)
    celular = models.BigIntegerField("TELÉFONO/ CELULAR", null=False, blank=False)
    email = models.EmailField(max_length=200)
    direcccion = models.CharField("DIRECCIÓN RESIDENCIA", max_length=100)
    c_emergencia = models.CharField("EN CASO DE EMERGENCIA LLAMAR A", max_length=100)
    n_emergencia = models.BigIntegerField("NÚMERO DE CONTACTO", null=False, blank=False)
    # semillero = models.ForeignKey(
    #     Semillero, on_delete=models.CASCADE, null=True, blank=True
    # )
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name_plural = "Coordinador"


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
        Coordinador,
        on_delete=models.CASCADE,
        related_name="semillerolist",
        verbose_name="Coordinador",
    )
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Integrante(models.Model):
    tipo_de_solictante = models.CharField("TIPO DE SOLICTANTE", max_length=100)
    nombre = models.CharField("NOMBRE COMPLETO", max_length=250)
    n_identificacion = models.BigIntegerField(
        "NÚMERO DE IDENTIFICACIÓN", primary_key=True
    )
    f_nacimiento = models.CharField("FECHA DE NACIMIENTO", max_length=100)
    direcccion = models.CharField("DIRECCIÓN RESIDENCIA", max_length=100)
    email = models.EmailField("CORREO ELECTRÓNICO", max_length=200)
    lugar_expedicion = models.CharField("LUGAR DE EXPEDICIÓN ID", max_length=100)
    lugar_nacimiento = models.CharField("LUGAR DE NACIMIENTO", max_length=100)
    celular = models.BigIntegerField("TELÉFONO/ CELULAR", null=False, blank=False)
    c_emergencia = models.CharField("EN CASO DE EMERGENCIA LLAMAR A", max_length=100)
    n_emergencia = models.BigIntegerField("NÚMERO DE CONTACTO", null=False, blank=False)
    semillero = models.ForeignKey(
        Semillero, on_delete=models.CASCADE, null=True, blank=True
    )
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.n_identificacion)
