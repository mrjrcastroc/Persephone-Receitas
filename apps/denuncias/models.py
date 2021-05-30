from django.db                   import models
from datetime                    import datetime
from usuarios.models             import Usuario
from django.contrib.auth.models  import User
from receitas.models             import Receita
from comentarios.models          import Comentarios

from django.urls                 import reverse_lazy, reverse
from django.shortcuts            import get_object_or_404, get_list_or_404, redirect

class CategoriaDenuncia(models.Model):
    titulo          = models.CharField(max_length=300)
    descricao       = models.TextField()
    acao_tomar      = models.CharField(max_length=300)
    data_categoria  = models.DateField(auto_now_add=True)
    ativa           = models.BooleanField(default = False)
    
    def __str__(self):
        return '%i - %s' %(self.id, self.titulo)

    def get_absolute_url(self):
        return reverse('perfil')

class DenunciaReceita(models.Model):
    receita                  = models.ForeignKey(Receita, related_name="receita_denuncia" , on_delete = models.CASCADE)
    titulo                   = models.CharField(max_length=300)
    usuario_denunciado       = models.ForeignKey(User, related_name = "usuario_denunciado_receita",   on_delete = models.CASCADE)
    usuario_efetuou_denuncia = models.ForeignKey(User, related_name = "usuario_efetuou_denuncia",     on_delete = models.CASCADE)
    texto                    = models.TextField()
    categoria_denuncia       = models.ForeignKey(CategoriaDenuncia, related_name = "categoria_denuncia", on_delete = models.CASCADE)
    data_denuncia            = models.DateField(auto_now_add=True)
    situacao                 = models.CharField(blank = True,max_length=200)
    resolvida                = models.BooleanField(default = False)

    def __str__(self):
        return  ' %i- %s - %s' %( self.id, self.titulo, self.categoria_denuncia)
    def get_absolute_url(self):
        return reverse('perfil')


class DenunciaComentario(models.Model):
    receita                  = models.ForeignKey(Receita, related_name="receita_comentario" , on_delete = models.CASCADE)
    comentario               = models.ForeignKey(Comentarios, related_name="denuncia_comentarios" , on_delete = models.CASCADE)
    titulo                   = models.CharField(max_length=300)
    usuario_denunciado       = models.ForeignKey(User, related_name = "usuario_denunciado_por_comentario",   on_delete = models.CASCADE)
    usuario_efetuou_denuncia = models.ForeignKey(User, related_name = "usuario_efetuou_denuncia_comentario",     on_delete = models.CASCADE)
    texto                    = models.TextField()
    categoria_denuncia       = models.ForeignKey(CategoriaDenuncia, related_name = "categoria_denuncia_c", on_delete = models.CASCADE)
    data_denuncia            = models.DateField(auto_now_add=True)
    situacao                 = models.CharField(blank = True,max_length=200)
    resolvida                = models.BooleanField(default = False)

    def __str__(self):
        return  ' %i- %s - %s' %( self.id, self.titulo, self.categoria_denuncia)
    def get_absolute_url(self):
        return reverse('perfil')
