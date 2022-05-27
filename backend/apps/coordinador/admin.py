from django.contrib import admin
from .models import Coordinador, Idioma, Informacion_C, Curso,  Experiencia, Proyecto, Participacion_P_I,  Resultado_D_I, Actividad_institucional, Actividad_i

# Register your models here.
admin.site.register(Coordinador)
admin.site.register(Idioma)
admin.site.register(Informacion_C)
admin.site.register(Curso )
admin.site.register(Experiencia)
admin.site.register(Proyecto)
admin.site.register(Participacion_P_I)
admin.site.register( Actividad_institucional)
admin.site.register( Actividad_i)
