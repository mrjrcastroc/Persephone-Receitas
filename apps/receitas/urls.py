from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('ranking_receita', ranking_receita, name='ranking_receita'),

    path('buscar', buscar, name='buscar'),

    path('CriarReceitaView/', CriarReceitaView.as_view(), name ='CriarReceita'),
    path('ReceitaView/edit/<int:pk>', EditarReceitaView.as_view(),    name ='EditarReceitaView'),
    path('ReceitaView//<int:pk>/remove', DeletaReceitaView.as_view(), name= 'DeletaReceitaView'),

    path('<int:receita_id>', receita, name='receita'),
    path('like_receita/<int:receita_id>', like_receita, name='like_receita'),

   
    path('comentario/<int:pk>', AdicionarCommentView.as_view(), name ='AdicionarCommentView'),
    path('comentario/edit/<int:pk>', EditarCommentView.as_view(), name ='EditarCommentView'),
    path('comentario/<int:pk>/remove', RemoverCommentView.as_view(), name='RemoverCommentView'),


]