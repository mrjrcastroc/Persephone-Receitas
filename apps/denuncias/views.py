from django.shortcuts            import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models  import User
from django.contrib              import auth, messages
from datetime                    import datetime
from django.http                 import HttpResponseRedirect
from django.urls                 import reverse_lazy, reverse

from denuncias.forms             import CategoriaDenunciaForms  , EditarCategoriaDenunciaForms
from denuncias.forms             import DenunciaReceitaForms    , DenunciaReceitaForms, ResolverDenunciaReceitaForms

from denuncias.models            import CategoriaDenuncia, DenunciaReceita
from receitas.models             import Receita

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


 
class CriarCategoriaDenunciaView(CreateView):
    model = CategoriaDenuncia
    form_class= CategoriaDenunciaForms
    template_name = 'denuncias/categorias/categoria_denuncia.html'
    sucess_url = reverse_lazy('CategoriaDenunciasListView')


class EditarCategoriaDenunciaView(UpdateView):
    model = CategoriaDenuncia
    form_class = EditarCategoriaDenunciaForms
    template_name = 'denuncias/categorias/editar_categoria_denuncia.html'
    sucess_url = reverse_lazy('CategoriaDenunciasListView')

class RemoverCategoriaDenunciaView(DeleteView):
    model = CategoriaDenuncia
    template_name = 'denuncias/categorias/deletar_categoria_denuncia.html'
    success_url = reverse_lazy('CategoriaDenunciasListView')



# Denunciar Receita

class CadastrarDenunciaReceitaView(CreateView):
    model = DenunciaReceita
    form_class= DenunciaReceitaForms
    template_name = 'denuncias/receitas/denuncia_receita.html'
    sucess_url = reverse_lazy('index')



class ResolverDenunciaReceitaView(UpdateView):
    model = DenunciaReceita
    form_class = ResolverDenunciaReceitaForms
    template_name = 'denuncias/receitas/resolver_denuncia_receita.html'
    sucess_url = reverse_lazy('index')

def visualizar_denuncias(request,id):
    receita = get_object_or_404(Receita, pk=id)

    contexto = {'receita':receita}        


    return render(request, 'denuncias/receitas/visualizar_denuncia_receita.html',contexto)


def CategoriaDenunciasListView(request):
	categoria_denuncia = CategoriaDenuncia.objects.all()
	return render(request, 'denuncias/categorias/listar_categoria_denuncias.html', {'categoria_denuncia':categoria_denuncia})


def ListarDenunciasListView(request):
	denuncia_receita = DenunciaReceita.objects.all()
	return render(request, 'denuncias/receitas/listar_denuncias_receita.html', {'denuncias_receita':denuncia_receita})



def denuncia_receita(request):
    return render(request,'denuncias/receitas/denuncia_receita.html')

def denuncia_comentario(request):
    return render(request,'denuncias/comentarios/denuncia_comentario.html')
