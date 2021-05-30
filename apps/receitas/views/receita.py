from django.shortcuts            import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models  import User
from django.contrib              import auth, messages
from datetime                    import datetime
from receitas.models             import Receita
from django.core.paginator       import Paginator, EmptyPage, PageNotAnInteger
from usuarios.models             import Usuario
from django.http                 import HttpResponseRedirect
from django.urls                 import reverse_lazy, reverse
from receitas.forms              import ReceitaForms, EditarReceitaForms
from comentarios.forms           import ComentariosForms
from comentarios.models          import Comentarios
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from receitas.filters import ReceitaFilter

from django.db.models import Count


def index(request):
    receitas  = Receita.objects.order_by('-data_receita').filter(publicada = True)

    meus_filtros = ReceitaFilter(request.GET, queryset=receitas)
    
    receitas = meus_filtros.qs

    paginator = Paginator(receitas, 6)

    page      = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina,
        'filtros':meus_filtros
    }

    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    usuario_id = receita.usuario
    usuario = get_object_or_404(Usuario, usuario_id = usuario_id)


    total_likes = receita.total_likes()

    liked = False

    if receita.likes.filter(id = request.user.id).exists():
        liked = True
    if request.user.is_authenticated:
        usuario_logado = get_object_or_404(Usuario, usuario_id = request.user.id)


        receita_a_exibir = {
            'receita' : receita,
            'usuario' : usuario,
            'likes': total_likes,
            'liked': liked,
            'usuario_logado':usuario_logado
        }
    
    else:
        receita_a_exibir = {
            'receita' : receita,
            'usuario' : usuario,
            'likes': total_likes,
            'liked': liked
        }


    return render(request, 'receitas/crud/receita.html', receita_a_exibir)





class CriarReceitaView(CreateView):
    form_class = ReceitaForms
    template_name = 'Receitas/crud/cadastro_receita.html'


class EditarReceitaView(UpdateView):
    model = Receita
    form_class = EditarReceitaForms
    template_name = 'Receitas/crud/edita_receita.html'
                            
    def process_image(request):

        # inputImage is the name attribute of the <input> tag in the html
        inImg = request.FILES["inputImage"].read()

        encoded = b64encode(inImg)
        mime = "image/jpg"
        mime = mime + ";" if mime else ";"
        input_image = "data:%sbase64,%s" % (mime, encoded)        

        return render(request, "Receitas/crud/edita_receita.html", {{ "input_image": input }})


class DeletaReceitaView(DeleteView):
    model = Receita
    template_name = 'Receitas/crud/deletar_receita.html'
    success_url = reverse_lazy('perfil')


class AdicionarCommentView(CreateView):
    form_class= ComentariosForms
    template_name = 'Receitas/comentarios/cadastrar_comentario.html'


class EditarCommentView(UpdateView):
    model = Comentarios
    form_class = ComentariosForms
    template_name = 'Receitas/comentarios/editar_comentario.html'
    sucess_url = reverse_lazy('index')

class RemoverCommentView(DeleteView):
    model = Comentarios
    template_name = 'Receitas/comentarios/remover_comentario.html'
    success_url = reverse_lazy('index')


def ranking_receita(request):

    receitas = Receita.objects.annotate(likes_count=Count("likes") + Count("comentarios") )
    receitas  = receitas.order_by('-likes_count', '-data_receita').filter(publicada = True)

    dados = {'receitas':receitas}
    
    return render(request,'ranking/ranking_receita.html',dados)


def campo_vazio(campo):
    return not campo.strip()


def like_receita(request, receita_id):
    receita = get_object_or_404(Receita, id = request.GET['receita_id'])
    liked = False

    if receita.likes.filter(id = request.user.id).exists():
        receita.likes.remove(request.user)
        likes = False

    else:
        receita.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('receita', args=[str(receita_id)])) 
