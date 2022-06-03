from ctypes import resize
from rest_framework import serializers
from apps.semillero_app.models import Semillero
#from apps.coordinador.models import Coordinador
#from apps.coordinador.api.serializers import CoordinadorSerializer
#realiza un mapeo del modelo Semillero 

class SemilleroSerializer(serializers.ModelSerializer):
    #semillerolist =CoordinadorSerializer(many=True, read_only=True)
    class Meta: 
        model = Semillero
        fields = '__all__'











# validador de campos 
# def column_logitud(values):
#     if len(values) < 2:
#         raise serializers.ValidationError('La direccion es demaciado corta')




# class SemilleroSerializer(serializers.Serializer):

#     #Solo lectura
#     id = serializers.IntegerField(read_only=True)
#     nombre = serializers.CharField()
#     facultad =serializers.CharField()
#     programa_academico = serializers.CharField()
#     investigacion =serializers.CharField()
#     investigacion_asociado = serializers.CharField()
#     tematica =serializers.CharField()
#     justificacion =serializers.CharField()
#     #coordinator = serializers.CharField()
#     #integrante = serializers.CharField()

#     def create(self, validated_data):
#         return Semillero.objects.create(**validated_data)

#     # mapemos para actulixar la Data
#     def update(self, instance, validated_data):

#         instance.nombre =  validated_data.get('nombre', instance.nombre )  
#         instance.facultad =  validated_data.get('facultad', instance.facultad)  
#         instance.programa_academico =  validated_data.get('programa_academico', instance.programa_academico)
#         instance.investigacion =  validated_data.get('investigacion', instance.investigacion)  
#         instance.investigacion_asociado =  validated_data.get('investigacion_asociado', instance.investigacion)
#         instance.tematica =  validated_data.get('tematica', instance.tematica)
#         instance.justificacion =  validated_data.get('justificacion', instance.justificacion) 
#         instance.save()

#         return instance 