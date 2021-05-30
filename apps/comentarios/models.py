from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from receitas.models import Receita
from usuarios.models import Usuario
from django.urls                 import reverse_lazy, reverse
from django.shortcuts            import  get_object_or_404, get_list_or_404, redirect


class Comentarios(models.Model):
    usuario        = models.ForeignKey(User, related_name = "usuario_comentario", on_delete = models.CASCADE)
    receita        = models.ForeignKey(Receita, related_name="comentarios" , on_delete = models.CASCADE)
    titulo         = models.CharField(max_length=300)
    comentario     = models.TextField()
    data_comentario = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %i' %(self.receita, self.comentario, self.id)

    def get_absolute_url(self):

        return reverse('perfil')
