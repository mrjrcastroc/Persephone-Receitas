from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 


admin.site.site_header = "Persephone Dashboard"
admin.site.site_title = 'Persephone Receitas'
admin.site.index_title ='Persephone Receitas'
admin.site.header_title ='Persephone Receitas'

urlpatterns = [
    path('', include('receitas.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('denuncias/', include('denuncias.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)