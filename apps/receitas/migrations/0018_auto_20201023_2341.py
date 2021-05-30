# Generated by Django 3.1.2 on 2020-10-24 02:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0017_auto_20201019_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='likes',
            field=models.ManyToManyField(related_name='receita_publicada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receita',
            name='categoria',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='receita',
            name='tempo_preparo',
            field=models.CharField(max_length=50),
        ),
    ]
