from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from datetime import datetime
from receitas.models import Receita



def buscar(request):

    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas2 = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    dados = {
        'receitas' : lista_receitas2
    }
    return render(request, 'receitas/resultado_busca.html', dados)


 
def CategoriasView(request, categorias):
    receitas = Receitas.objects.filter(categoria = categoria, publicada = True)
    dados = {
        'categoria': categoria,
        'receitas': receita
    }

    return render(request, 'receitas/resultado_busca.html', dados)   