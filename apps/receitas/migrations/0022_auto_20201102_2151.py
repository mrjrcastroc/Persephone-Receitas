# Generated by Django 3.1.2 on 2020-11-03 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0021_auto_20201102_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.TextField(default='5'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Ingredientes',
        ),
    ]
