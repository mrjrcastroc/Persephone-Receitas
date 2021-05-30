from django.urls import path


from .views import *

urlpatterns = [
    path('CriarCategoriaDenunciaView/', CriarCategoriaDenunciaView.as_view(), name ='CriarCategoriaDenunciaView'),
    path('denuncia/edit/<int:pk>', EditarCategoriaDenunciaView.as_view(), name ='EditarCategoriaDenunciaView'),
    path('denuncia//<int:pk>/remove', RemoverCategoriaDenunciaView.as_view(), name='RemoverCategoriaDenunciaView'),
    path('categoria_denuncia/',CategoriaDenunciasListView, name = 'CategoriaDenunciasListView'),

    path('denuncia/',ListarDenunciasListView, name = 'ListarDenunciasListView'),

    path('denunciaReceitaView/<int:pk>', CadastrarDenunciaReceitaView.as_view(), name ='CadastrarDenunciaReceitaView'),
    path('denunciaReceitaViewEdit/edit/<int:pk>', ResolverDenunciaReceitaView.as_view(), name ='ResolverDenunciaReceitaView'),
    
    path('<int:id>', visualizar_denuncias, name='visualizar_denuncia'),
    path('denuncia_receita', denuncia_receita, name='denuncia_receita'),
    path('denuncia_comentario', denuncia_comentario, name='denuncia_comentario'),

]

