from django.db import models
from datetime import datetime
from django.contrib.auth.models  import User
from django.urls import reverse

class Usuario(models.Model):

    CATEGORIA = (
      ('Leigo', 'Leigo'),
      ('Iniciante', 'Iniciante'),
      ('Intermediário', 'Intermediário'),
      ('Avançado', 'Avançado'),
      ('Profissional', 'Profissional')

    )
    usuario_id       = models.OneToOneField(User, null = True, on_delete = models.CASCADE, related_name = 'usuario_cadastrado')
    categoria_chefe  = models.CharField (max_length = 25, choices = CATEGORIA, blank = False, default='Leig')
    foto_usuario     = models.ImageField(upload_to = 'static/fotos/%d/%m/%Y/', blank = True)
    descricao        = models.TextField()
    dt_criacao       = models.DateField (default    = datetime.now,      blank = True)
    avaliacao        = models.ManyToManyField(User, related_name = 'avaliacao_chefe')
    def __str__(self):
      return self.categoria_chefe
