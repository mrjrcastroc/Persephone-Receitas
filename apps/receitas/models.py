from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields             import RichTextField
from django.urls import reverse

CATEGORIA = (
      ('Bolos e Tortas','Bolos e Tortas'),
      ('Carnes','Carnes'),
      ('Aves','Aves'),
      ('Peixes e Frutos do Mar','Peixes e Frutos do Mar'),
      ('Saladas e Molhos', 'Saladas e Molhos'),
      ('Sopas','Sopas'),
      ('Massas', 'Massas'),
      ('Bebidas', 'Bebidas'),
      ('Doces e Sobremesas','Doces e Sobremesas'),
      ('Lanches', 'Lanches'),
      ('Fitness', 'Fitness'),
      ('Outros' , 'Outros'),
      )

valor_estimado    = (
      ('Até R$ 50,00','Até R$ 50,00' ),
      ('Entre R$ 50,00 e R$ 100,00','Entre R$ 50,00 e R$ 100,00'),
      ('Entre R$ 100,00 e R$ 150,00','Entre R$ 100,00 e R$ 150,00'),
      ('Entre R$ 150,00 e R$ 200,00','Entre R$ 150,00 e R$ 200,00'),
      ('Superior a R$ 200,00','Superior a R$ 200,00'),

    )
  

nivel = (
      ('Leigo', 'Leigo'),
      ('Iniciante', 'Iniciante'),
      ('Intermediário', 'Intermediário'),
      ('Avançado', 'Avançado'),
      ('Profissional', 'Profissional')

    )

rendimento = (
      ('Até 5 pessoas' ,'Até 5 pessoas'  ),
      ('Até 10 pessoas','Até 10 pessoas' ),
      ('Até 15 pessoas','Até 15 pessoas' ),
      ('Até 20 pessoas','Até 20 pessoas' ),
      ('Até 50 pessoas','Até 50 pessoas' ),

    )

tempo_preparo = (
      ('Até 10 minutos', 'Até 10 minutos'),
      ('Até 20 minutos,', 'Até 20 minutos,'),
      ('Até 30 minutos', 'Até 30 minutos'),
      ('Até 60 minutos', 'Até 60 minutos'),
      ('Superior 60 minutos','Superior 60 minutos' ),
    )



class Receita(models.Model):
    usuario        = models.ForeignKey(User,  related_name = 'receita_x_usuario', on_delete = models.CASCADE)
    nome_receita   = models.CharField(max_length = 300)
    descricao      = models.TextField()
    modo_preparo   = models.TextField()
    tempo_preparo  = models.CharField(max_length = 250, choices = tempo_preparo)
    categoria      = models.CharField(max_length = 250, choices = CATEGORIA)
    rendimento     = models.CharField(max_length = 250, choices = rendimento)
    foto_receita   = models.ImageField(upload_to = 'static/fotos/%d/%m/%Y/', blank = True)
    foto_receita2  = models.ImageField(upload_to = 'static/fotos/%d/%m/%Y/', blank = True)
    foto_receita3  = models.ImageField(upload_to = 'static/fotos/%d/%m/%Y/', blank = True)
    valor_estimado = models.CharField(max_length = 250, choices=valor_estimado)
    dificuldade    = models.CharField(max_length = 250, choices=nivel)
    data_receita   = models.DateField(default    = datetime.now,      blank = True)
    publicada      = models.BooleanField(default = True)
    likes          = models.ManyToManyField(User, related_name = 'receita_publicada')

    def __str__(self):
      return self.nome_receita

    def total_likes(self):
      return self.likes.count()
  
    def get_absolute_url(self):
      return reverse('index')
