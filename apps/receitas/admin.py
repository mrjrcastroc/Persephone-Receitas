from django.contrib import admin
from .models import Receita

# Register your models here.

class ListandoReceitas(admin.ModelAdmin):
    list_display       = ('id', 'usuario','nome_receita',  'tempo_preparo','publicada') 
    list_display_links = ('id', 'nome_receita', 'usuario')
    search_fields      = ('nome_receita', 'publicada','usuario')
    list_per_page      = 4
    list_editable      = ('publicada',)


admin.site.register(Receita ,ListandoReceitas)
