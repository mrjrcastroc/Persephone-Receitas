# Generated by Django 3.1.2 on 2020-10-15 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20201014_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='dt_alteracao',
        ),
    ]
