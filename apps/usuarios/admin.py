from django.contrib import admin
from .models import Usuario

# Register your models here.

class ListandoPessoas(admin.ModelAdmin):
    list_display       = ('id','usuario_id','categoria_chefe')
    list_display_links = ('id','usuario_id','categoria_chefe')
    search_fields = ('categoria_chefe','usuario_id',)
    list_per_page = 4

admin.site.register(Usuario, ListandoPessoas)