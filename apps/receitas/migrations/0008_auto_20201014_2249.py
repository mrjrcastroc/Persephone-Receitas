# Generated by Django 3.1.2 on 2020-10-15 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0007_receita_avaliacao_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='avaliacao_receita',
            field=models.FloatField(default=0),
        ),
    ]