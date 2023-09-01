from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Proyecto_Final import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehiculos.urls')),
]



urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)