# Generated by Django 3.1.2 on 2020-11-11 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_auto_20201110_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='categoria_chefe',
            field=models.CharField(choices=[('Leigo', 'Leigo'), ('Iniciante', 'Iniciante'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado'), ('Profissional', 'Profissional')], default='Leig', max_length=25),
        ),
    ]