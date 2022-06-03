from django.contrib import admin
from .models import (
    Semillero,
    Coordinador,
    Integrante,
)


@admin.register(Semillero)
class SemilleroAdmin(admin.ModelAdmin):
    """Admin View for Semillero"""

    list_display = ("id", "nombre", "coordinator")
    list_filter = [
        "coordinator",
    ]


@admin.register(Coordinador)
class CoordinadorAdmin(admin.ModelAdmin):
    """Admin View for Coordinador"""

    list_display = ("n_identificacion",)


@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    """Admin View for Integrante"""

    list_display = (
        "pk",
        "semillero",
    )
