from django.db import models

# Create your models here.
class Actividad_i(models.Model):
    nombre_c = models.CharField('NOMBRE GRUPO/ COMITÉ', max_length=100)
    actividad = models.CharField('ACTIVIDAD O TEMA', max_length=100)
    tipo = models.CharField('TIPO DE VINCULACIÓN (Rol que desempeño)', max_length=100)
    fecha = models.CharField('FECHA', max_length=100)

    def __str__(self):
        return self.nombre_c


class Actividad_institucional(models.Model):
    participacion_c = models.IntegerField('Participa en Comité o Grupo de Trabajo', null=False, blank=False, choices=[(1, 'SI'), (2, 'NO')])
    actividad = models.ForeignKey( Actividad_i, on_delete=models.CASCADE, null=False, blank=True)
    
    def __str__(self):
        return str(self.participacion_c)


class Resultado_D_I(models.Model):
    tipo = models.CharField('TIPO', max_length=100)
    nombre = models.CharField('NOMBRE', max_length=100)
    publicado =  models.CharField('PUBLICADO EN', max_length=100)
    año = models.CharField('AÑO', max_length=100)

    def __str__(self):
        return self.tipo


class Participacion_P_I(models.Model):
    nombre_proyecto = models.CharField('NOMBRE PROYECTO', max_length=100)
    institucion =  models.CharField('INSTITUCIÓN', max_length=100)
    tipo_de_vinculacion = models.CharField('TIPO DE VINCULACIÓN (Rol desempeñado)', max_length=100)
    año = models.CharField('AÑO', max_length=100)

    def __str__(self):
        return self.nombre_proyecto


class Proyecto(models.Model):
    proyecto_i = models.IntegerField('Participa en Comité o Grupo de Trabajo', null=False, blank=False, choices=[(1, 'SI'), (2, 'NO')])
    participacion_p_i = models.ForeignKey( Participacion_P_I, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return str(self.proyecto_i)


class Experiencia(models.Model):
    cvlac = models.IntegerField('¿Tiene CvLAC registrado en Colciencias?', null=False, blank=False, choices=[(1, 'SI'), (2, 'NO')])
    proyecto_i =  models.OneToOneField(Proyecto, on_delete=models.CASCADE, null=False, blank=True)
    resultado_d_i = models.ForeignKey( Resultado_D_I, on_delete=models.CASCADE, null=False, blank=True)
    Actividad_i =  models.OneToOneField( Actividad_institucional, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return str(self.cvlac)


class Curso(models.Model):
    tematica = models.CharField('TEMÁTICA',max_length=250)
    institucion = models.CharField('INSTITUCIÓN',max_length=250)
    horas = models.CharField('HORAS',max_length=250)
    fecha = models.CharField('FECHA', max_length=100)

    def __str__(self):
        return self.tematica


class Informacion_C(models.Model):
    nivel = models.IntegerField('Indique el Nivel Alcanzado', null=False, blank=False, choices=[(1, 'BÁSICO'), (2, 'INTERMEDIO'), (3, 'AVANZADO')])
    information = models.TextField('JUSTIFICACIÓN DEL SEMILLERO DE INVESTIGACIÓN', max_length=2000)
    
    def __str__(self):
        return str(self.nivel)

class Idioma(models.Model):
    lengua = models.CharField('Lengua', max_length=100)
    nivel = models.IntegerField('Indique el Nivel Alcanzado', null=False, blank=False, choices=[(1, 'BÁSICO'), (2, 'INTERMEDIO'), (3, 'AVANZADO')])

    def __str__(self):
        return str(self.lengua)


class Coordinador(models.Model):
    n_identificacion = models.BigIntegerField('NÚMERO DE IDENTIFICACIÓN',primary_key=True)
    nombre = models.CharField('NOMBRE COMPLETO',max_length=250)
    f_nacimiento = models.CharField('FECHA DE NACIMIENTO',max_length=100)
    lugar_expedicion = models.CharField('LUGAR DE EXPEDICIÓN ID',max_length=100)
    lugar_nacimiento = models.CharField('LUGAR DE NACIMIENTO',max_length=100)
    celular = models.BigIntegerField('TELÉFONO/ CELULAR',null=False, blank=False)
    email = models.EmailField(max_length=200)
    direcccion = models.CharField('DIRECCIÓN RESIDENCIA',max_length=100)
    email = models.EmailField('CORREO ELECTRÓNICO',max_length=200)
    c_emergencia = models.CharField('EN CASO DE EMERGENCIA LLAMAR A',max_length=100)
    n_emergencia = models.BigIntegerField('NÚMERO DE CONTACTO',null=False, blank=False)
    idioma = models.ForeignKey( Idioma, on_delete=models.CASCADE, null=False, blank=True)
    informacion_academica = models.ForeignKey( Informacion_C, on_delete=models.CASCADE, null=False, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.n_identificacion) 
