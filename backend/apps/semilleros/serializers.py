from rest_framework import serializers
from .models import (
    Coordinador,
    Semillero,
    Integrante,
)


class CoordinadorSerializer(serializers.ModelSerializer):
    # semillerolist = SemilleroSerializer(many=True, read_only=True)

    class Meta:
        model = Coordinador
        fields = [
            "n_identificacion",
            "nombre",
            "f_nacimiento",
            "lugar_expedicion",
            "lugar_nacimiento",
            "celular",
            "email",
            "direcccion",
            "c_emergencia",
            "n_emergencia",
            "create_at",
        ]


class SemilleroSerializer(serializers.ModelSerializer):
    # semillerolist =CoordinadorSerializer(many=True, read_only=True)
    # coordinator = CoordinadorSerializer(many=False)
    coordinator = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Coordinador.objects.all()
    )

    class Meta:
        model = Semillero
        fields = [
            "id",
            "nombre",
            "facultad",
            "programa_academico",
            "investigacion",
            "investigacion_asociado",
            "tematica",
            "justificacion",
            "coordinator",
        ]


class SemilleroGetSerializer(serializers.ModelSerializer):
    coordinator = CoordinadorSerializer(many=False)

    class Meta:
        model = Semillero
        fields = [
            "id",
            "nombre",
            "facultad",
            "programa_academico",
            "investigacion",
            "investigacion_asociado",
            "tematica",
            "justificacion",
            "coordinator",
        ]


class IntegranteSerializer(serializers.ModelSerializer):
    # semillerolist = SemilleroSerializer(many=True, read_only=True)

    class Meta:
        model = Integrante
        fields = [
            "tipo_de_solictante",
            "nombre",
            "n_identificacion",
            "f_nacimiento",
            "direcccion",
            "email",
            "lugar_expedicion",
            "lugar_nacimiento",
            "celular",
            "c_emergencia",
            "n_emergencia",
            # "semillero",
        ]
