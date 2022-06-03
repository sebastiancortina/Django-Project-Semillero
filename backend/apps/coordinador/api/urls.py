from django.contrib import admin
from django.urls import path
from apps.coordinador.api.views import SemilleroListCUA, SemilleroDetalleCUA

urlpatterns = [
    path('list/', SemilleroListCUA.as_view(), name='semillero-list' ),
    path('<int:id>/', SemilleroDetalleCUA.as_view(), name=' semillero-detalle'),
    

]