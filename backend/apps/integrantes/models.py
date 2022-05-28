from django.db import models

# Create your models here.
class Aval(models.Model):
    observaciones = models.TextField('OBSERVACIONES')
    firma_d = models.CharField('DOCENTE COORDINADOR DEL SEMILLERO', max_length=100)
    confirmar_d = models.IntegerField( null=False, blank=False, choices=[(1, 'APROBADO'), (2, 'NEGADO')])
    firma_c = models.CharField('COMITÉ DE INVESTIGACIONES DE LA FACULTAD', max_length=100)
    confirmar_c = models.IntegerField( null=False, blank=False, choices=[(1, 'APROBADO'), (2, 'NEGADO')])

    def __str__(self):
        return str(self.id)


class Semillero_de_interes(models.Model):
    nombre = models.CharField('Nombre del semillero de interés', max_length=100)
    linea_i = models.CharField('Nombre del semillero de interés', max_length=100)
    numero_h =  models.IntegerField('Número de horas semanales que estaría dispuesto a dedicar al proyecto de investigación', null=False, blank=False, choices=[(1, 'BÁSICO'), (2, 'INTERMEDIO'), (3, 'AVANZADO')])
    tipo_s = models.IntegerField('Tipo de Semillero al que aplica', null=False, blank=False, choices=[(1, 'Fase Única'), (2, 'Fase Doble'), (3, 'Fase Triple')])

    def __str__(self):
        return self.nombre

class Actividad_i(models.Model):
    nombre_c = models.CharField('NOMBRE GRUPO/ COMITÉ', max_length=100)
    actividad = models.CharField('ACTIVIDAD O TEMA', max_length=100)
    tipo = models.CharField('TIPO DE VINCULACIÓN (Rol que desempeño)', max_length=100)
    fecha = models.CharField('FECHA', max_length=100)

    def __str__(self):
        return self.nombre_c

class Actividad_institucional(models.Model):
    participacion_c = models.BooleanField('Participa en Comité o Grupo de Trabajo', default=False)
    actividad = models.ForeignKey( Actividad_i, on_delete=models.CASCADE)
    
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

class Proyecto(models.Model):
    proyecto_i = models.BooleanField('¿Ha participado en Proyectos de Investigación?', default=False)
    participacion_p_i = models.ForeignKey( Participacion_P_I, on_delete=models.CASCADE, null=False, blank=True)
    resultado_d_i =  models.ForeignKey( Resultado_D_I, on_delete=models.CASCADE, null=False, blank=True)
    def __str__(self):
        return str(self.proyecto_i)

class Experiencia(models.Model):
    cvlac = models.BooleanField('¿Tiene CvLAC registrado en Colciencias?', default=False)


    def __str__(self):
        return str(self.cvlac)

class Curso(models.Model):
    tematica = models.CharField('TEMÁTICA',max_length=250)
    institucion = models.CharField('INSTITUCIÓN',max_length=250)
    horas = models.CharField('HORAS',max_length=250)
    fecha = models.CharField('FECHA', max_length=100)
    
    def __str__(self):
        return self.tematica

class Informacion_i(models.Model):
    c_investigacion = models.IntegerField('¿Ha realizado cursos de formación de investigación?', null=False, blank=False, choices=[(1, 'SI'), (2, 'NO')])
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Informacion_E(models.Model):
    programa =  models.CharField('PROGRAMA', max_length=250)
    año = models.CharField('AÑO INGRESO', max_length=100)
    semestre =  models.CharField('SEMESTRE ACTUAL', max_length=100)
    fecha = models.CharField('FECHA DE GRADO', max_length=100)
    
    def __str__(self):
        return str(self.programa)


class Idioma(models.Model):
    lengua = models.CharField('Lengua', max_length=100)
    nivel = models.IntegerField('Indique el Nivel Alcanzado', null=False, blank=False, choices=[(1, 'BÁSICO'), (2, 'INTERMEDIO'), (3, 'AVANZADO')])

    def __str__(self):
        return str(self.lengua)

class Integrante(models.Model):
    n_identificacion = models.BigIntegerField(primary_key=True ,null=False, blank=False)
    solicitante = models.CharField('TIPO DE SOLICTANTE', max_length=250)
    nombre = models.CharField(max_length=100)
    f_nacimiento = models.CharField('FECHA DE NACIMIENTO',max_length=100)
    lugar_expedicion = models.CharField('LUGAR DE EXPEDICIÓN ID',max_length=100)
    lugar_nacimiento = models.CharField('LUGAR DE NACIMIENTO',max_length=100)
    celular = models.BigIntegerField()
    direcccion = models.CharField('DIRECCIÓN RESIDENCIA',max_length=100)
    email = models.EmailField('CORREO ELECTRÓNICO',max_length=200)
    c_emergencia = models.CharField('EN CASO DE EMERGENCIA LLAMAR A',max_length=100)
    n_emergencia = models.BigIntegerField('NÚMERO DE CONTACTO',null=False, blank=False)
    idioma = models.ForeignKey( Idioma, on_delete=models.CASCADE, null=False, blank=True)
    informacion_academica = models.ForeignKey( Informacion_E, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return str(self.n_identificacion)










"""
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
"""