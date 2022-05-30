from rest_framework import serializers

class SemilleroSerializer(serializers.Serializer):

    #Solo lectura
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    facultad =serializers.CharField()
    programa_academico = serializers.CharField()
    investigacion =serializers.CharField()
    investigacion_asociado = serializers.CharField()
    tematica =serializers.CharField()
    justificacion =serializers.CharField()
    coordinator = serializers.CharField()
    integrante = serializers.CharField()
    