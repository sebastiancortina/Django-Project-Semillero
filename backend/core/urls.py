from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.semilleros.urls")),
    # path('semillero/', include('apps.semillero_app.apis.urls')),
    # path('coordinador/', include('apps.coordinador.api.urls'))
]
