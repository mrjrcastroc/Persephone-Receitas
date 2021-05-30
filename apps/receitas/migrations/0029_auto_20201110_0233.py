# Generated by Django 3.1.2 on 2020-11-10 05:33

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0028_auto_20201110_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='categoria',
            field=models.CharField(choices=[('Bolos e Tortas', 'Bolos e Tortas'), ('Carnes', 'Carnes'), ('Aves', 'Aves'), ('Peixes e Frutos do Mar', 'Peixes e Frutos do Mar'), ('Saladas e Molhos', 'Saladas e Molhos'), ('Sopas', 'Sopas'), ('Massas', 'Massas'), ('Bebidas', 'Bebidas'), ('Doces e Sobremesas', 'Doces e Sobremesas'), ('Lanches', 'Lanches'), ('Fitness', 'Fitness'), ('Outros', 'Outros')], default='Outros', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='receita',
            name='dificuldade',
            field=models.CharField(choices=[('Leigo', 'Leigo'), ('Iniciante', 'Iniciante'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado'), ('Profissional', 'Profissional')], default='Leigo', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(upload_to='static/fotos/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='foto_receita2',
            field=models.ImageField(upload_to='static/fotos/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='foto_receita3',
            field=models.ImageField(upload_to='static/fotos/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='receita_publicada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receita',
            name='modo_preparo',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='receita',
            name='rendimento',
            field=models.CharField(choices=[('Até 5 pessoas', 'Até 5 pessoas'), ('Até 10 pessoas', 'Até 10 pessoas'), ('Até 15 pessoas', 'Até 15 pessoas'), ('Até 20 pessoas', 'Até 20 pessoas'), ('Até 50 pessoas', 'Até 50 pessoas')], max_length=200),
        ),
        migrations.AlterField(
            model_name='receita',
            name='tempo_preparo',
            field=models.CharField(choices=[('Até 10 minutos', 'Até 10 minutos'), ('Até 20 minutos,', 'Até 20 minutos,'), ('Até 30 minutos', 'Até 30 minutos'), ('Até 60 minutos', 'Até 60 minutos'), ('Superior 60 minutos', 'Superior 60 minutos')], default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]