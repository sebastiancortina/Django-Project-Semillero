from django.db import models
from apps.semillero_app.models import Semillero
# Create your models here.
# class Recibido_C(models.Model):
#     firma_s = models.CharField('Firma Solicitante', max_length=100)
#     firma_r = models.CharField('Firma Recibido', max_length=100)

# class Aval(models.Model):
#     observaciones = models.TextField('JUSTIFICACIÓN DEL SEMILLERO DE INVESTIGACIÓN')
#     firma_d = models.CharField('Firma y Fecha - DOCENTE COORDINADOR DEL SEMILLERO', max_length=100)
#     aval_d = models.IntegerField( null=False, blank=False, choices=[(1, 'APROBADO'), (2, 'NEGADO')])
#     firma_c = models.CharField('Firma y Fecha - COMITÉ DE INVESTIGACIONES DE LA FACULTAD', max_length=100)
#     aval_d = models.IntegerField( null=False, blank=False, choices=[(1, 'APROBADO'), (2, 'NEGADO')])
#     recibido_c = models.OneToOneField(Recibido_C,  on_delete=models.CASCADE)


# class Linea(models.Model):
#     nombre = models.CharField('Nombre del semillero de interés (No es obligatorio): ', max_length=100)
#     linea = models.CharField('Línea y sublínea de investigación', max_length=100)
#     numero_h = models.CharField('Número de horas semanales que estaría dispuesto a dedicar al proyecto de investigación', max_length=100)
#     tipo = models.IntegerField('Tipo de Semillero al que aplica', null=False, blank=False, choices=[(1, 'Fase Única'), (2, 'Fase Doble'), (3, 'Fase Triple')])

#     def __str__(self):
#         return self.nombre

# class Actividad(models.Model):
#     nombre = models.CharField('NOMBRE GRUPO/ COMITÉ', max_length=100)
#     actividad = models.CharField('ACTIVIDAD O TEMA', max_length=100)
#     tipo_vinculacion = models.CharField('TIPO DE VINCULACIÓN (Rol que desempeño)', max_length=100)
#     fecha =  models.CharField('FECHA', max_length=100)

#     def __str__(self):
#         return self.nombre


# class Actividades_I_I(models.Model):
#     participado = models.IntegerField('Participa en Comité o Grupo de Trabajo', null=False, blank=False, choices=[(1, 'SI'), (2, 'NO')])
#     actividad = models.ForeignKey( Actividad,  on_delete=models.CASCADE)

#     def __str__(self):
#         return self.participado

# class Resultados_D_I(models.Model):
#     tipo = models.CharField('TIPO', max_length=100)
#     nombre = models.CharField('NOMBRE', max_length=100)
#     publicado = models.CharField('PUBLICADO EN', max_length=100)
#     ano_r = models.CharField('AÑO', max_length=100)

#     def __str__(self):
#         return self.tipo


# class Proyecto_I_P(models.Model):
#     nombre = models.CharField(max_length=100)
#     institucion = models.CharField(max_length=100)
#     tipo = models.CharField(max_length=100)
#     ano_p = models.CharField(max_length=100)
#     resultados_d_i = models.OneToOneField(Resultados_D_I,  on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.nombre


# class Experiencia_I(models.Model):
#     formacion_i = models.IntegerField('¿Tiene CvLAC registrado en Colciencias?', null=False, blank=False, choices=[(1, 'SI'), (2, 'NO')])
#     formacion_p = models.BooleanField('¿Ha participado en Proyectos de Investigación?', default=True)
#     proyecto_i_p = models.ForeignKey(Proyecto_I_P, on_delete=models.CASCADE, null=False, blank=True)
    
#     def __str__(self):
#         return self.formacion_i


# class Curso_F(models.Model):
#     nombre = models.CharField(max_length=100)
#     institucion = models.CharField(max_length=100)
#     hora = models.CharField(max_length=100)
#     fecha = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.nombre)


# class Curso_F_I(models.Model):
#     formacion_i = models.IntegerField('¿Ha realizado cursos de formación de investigación?', null=False, blank=False, choices=[(1, 'SI'), (2, 'NO')])
#     curso_f =  models.ForeignKey(Curso_F, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.formacion_i) 
    

    
# class Informacion_E(models.Model):
#     programa =  models.CharField('PROGRAMA', max_length=100)
#     ano_i = models.CharField('AÑO INGRESO', max_length=100)
#     semestre = models.CharField('SEMESTRE ACTUAL', max_length=100)
#     grado = models.CharField('FECHA DE GRADO', max_length=100)

#     def __str__(self):
#         return str(self.programa) 


# class Idioma(models.Model):
#     lengua = models.CharField('Lengua', max_length=100)
#     nivel = models.IntegerField('Indique el Nivel Alcanzado', null=False, blank=False, choices=[(1, 'BASICO'), (2, 'INTERMEDIO'), (3, 'AVANZADO')])

#     def __str__(self):
#         return str(self.lengua) 


class Integrante(models.Model):
    tipo_de_solictante =  models.CharField('TIPO DE SOLICTANTE', max_length=100)
    nombre = models.CharField('NOMBRE COMPLETO',max_length=250)
    n_identificacion = models.BigIntegerField('NÚMERO DE IDENTIFICACIÓN',primary_key=True)
    f_nacimiento = models.CharField('FECHA DE NACIMIENTO',max_length=100)
    direcccion = models.CharField('DIRECCIÓN RESIDENCIA',max_length=100)
    email = models.EmailField('CORREO ELECTRÓNICO',max_length=200)
    lugar_expedicion = models.CharField('LUGAR DE EXPEDICIÓN ID',max_length=100)
    lugar_nacimiento = models.CharField('LUGAR DE NACIMIENTO',max_length=100)
    celular = models.BigIntegerField('TELÉFONO/ CELULAR',null=False, blank=False)
    c_emergencia = models.CharField('EN CASO DE EMERGENCIA LLAMAR A',max_length=100)
    n_emergencia = models.BigIntegerField('NÚMERO DE CONTACTO',null=False, blank=False)
    semillero = models.ForeignKey(Semillero, on_delete=models.CASCADE,  null=True, blank=True)
    # idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, null=False, blank=True)
    # informacion_e = models.OneToOneField(Informacion_E, on_delete=models.CASCADE)
    # curso_f_i = models.OneToOneField(Curso_F_I, on_delete=models.CASCADE)
    # experiencia_i = models.OneToOneField(Experiencia_I, on_delete=models.CASCADE)
    # linea =  models.OneToOneField(Linea, on_delete=models.CASCADE)
    # aval =  models.OneToOneField(Aval, on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.n_identificacion) 