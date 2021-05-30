from django.urls import path
from . import views
from usuarios.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name='login'),
    path('perfil',views.perfil, name ='perfil'),
    path('logout', views.logout, name='logout'),
    path('avaliacao_chefe/<int:receita_id>', avaliacao_chefe, name='avaliacao_chefe'),
    path('ranking_chefe', ranking_chefe, name='ranking_chefe'),

# ------------------------------------CRUD USER ----------------------------------------------
    path('cadastro_usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('password/', PasswordsChangeView.as_view(template_name='Usuarios/redefinir_senha.html'), name='PasswordsChangeView'),
	path('password_success', views.password_success, name="password_success"),

# ------------------------------------CRUD PERFIL----------------------------------------------

	path('create_profile_page/', CreateProfilePageView.as_view(), name='criar_perfil'),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
	path('<int:pk>/deleta_profile_page/', DeletaProfilePageView.as_view(), name='DeletaProfilePageView'),

# ------------------------------------REDEFINIR SENHA----------------------------------------------

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="Usuarios/esqueci_senha/password_reset.html"),
     name="reset_password"),



    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="Usuarios/esqueci_senha/password_reset_sent.html"), 
        name="password_reset_done"),

    #path('reset/<uidb64>/<token>/',
    # auth_views.PasswordResetConfirmView.as_view(template_name="Usuarios/reset/password_change_form.html", reset_url_token='password_reset_confirm'), 
    # name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="Usuarios/esqueci_senha/password_reset_done.html"), 
        name="password_reset_complete"),


]