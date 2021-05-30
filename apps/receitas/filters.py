import django_filters
from .models import Receita
from django_filters import CharFilter

class ReceitaFilter(django_filters.FilterSet):

    ingredientes = CharFilter(field_name='ingredientes', lookup_expr='icontains', label="Pesquisar por Ingredientes")
    
    class Meta:
        model = Receita
        fields = ('tempo_preparo','categoria','rendimento','valor_estimado','dificuldade')