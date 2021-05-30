from django.shortcuts           import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.views import generic

from django.contrib             import auth, messages
from datetime                   import datetime
from receitas.models            import Receita
from usuarios.models            import Usuario
from django.urls                import reverse_lazy, reverse

from usuarios.forms             import CriarUsuarioForms, UserRegisterForm, PasswordChangingForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http                 import HttpResponseRedirect
from django.db.models import Count



def logout(request):
    auth.logout(request)    
    return redirect('index')


def perfil(request):
    if request.user.is_authenticated:
        usuario_id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(usuario = usuario_id)
        usuario = get_object_or_404(Usuario, usuario_id = usuario_id)

        dados = {
            'receitas': receitas,
            'usuario': usuario
        }

        return render(request,'usuarios/perfil.html', dados)
    else:
        return redirect('index')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if campo_vazio(email):
            messages.error(request, 'O campo e-mail não pode ficar em branco')
            return redirect('login')

        if campo_vazio(senha):
            messages.error(request, 'O campo senha não pode ficar em branco')
            return redirect('login')


        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)    

            if user is not None:
                auth.login(request, user)
                print('Login realizado om sucesso ')
                return redirect('index')
            else:
                messages.error(request, 'Senha invalida. Digite a sua senha novamene.')
                return redirect('login')


    return render(request,'usuarios/login.html')


# FUNÇÕES DE VERIFICAÇÃO
def campo_vazio(campo):
    return not campo.strip()

def verifica_senha(senha, senha2):

    return senha != senha2


def campo_vazio(campo):
    return not campo.strip()


    

def cadastro_usuario(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criar_perfil')
    else:
        form = UserRegisterForm()

    return render(request,'Usuarios/crud_usuario/cadastro_usuario.html', {'form': form} )


class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	#foom_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')
	#success_url = reverse_lazy('home')
def password_success(request):
	return render(request, 'Usuarios/troca_senha/redefinir_senha_sucesso.html', {})

class CreateProfilePageView(CreateView):
	model = Usuario
	form_class = CriarUsuarioForms
	template_name = "Usuarios/crud_perfil/cadastro_perfil.html"
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditProfilePageView(UpdateView):
	model = Usuario
	template_name = "Usuarios/crud_perfil/cadastro_perfil.html"
	success_url = reverse_lazy('perfil')
	fields = ('categoria_chefe', 'foto_usuario')    

class DeletaProfilePageView(DeleteView):
	model = User
	template_name = "Usuarios/crud_perfil/deleta_perfil.html"
	success_url = reverse_lazy('index')


def avaliacao_chefe(request, receita_id):
    usuario = get_object_or_404(Usuario, usuario_id = request.user.id)
    avaliado = False

    if usuario.avaliacao.filter(id = request.user.id).exists():
        usuario.avaliacao.remove(request.user)
        avaliado = False

    else:
        usuario.avaliacao.add(request.user)
        avaliado = True
    
    return HttpResponseRedirect(reverse('receita', args=[str(receita_id)])) 

def ranking_receita(request):

    receitas = Receita.objects.annotate(likes_count=Count("likes") + Count("comentarios") )
    receitas  = receitas.order_by('-likes_count', '-data_receita').filter(publicada = True)

    dados = {'receitas':receitas}
    
    return render(request,'ranking/ranking_receita.html',dados)

def ranking_chefe(request):

    perfil  = Usuario.objects.annotate(avaliacao_che=Count("avaliacao") )
    perfil  = perfil.order_by('-avaliacao_che', '-dt_criacao')
    
    usuario = User.objects.annotate(qtd_receitas = Count("receita_x_usuario"))

    usuario = usuario.order_by('-receita_x_usuario')
    dados = {'perfil':perfil,
             'usuario': usuario}

 
    return render(request,'ranking/ranking_chefe.html', dados)
