# Generated by Django 3.1.2 on 2020-10-25 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0003_auto_20201024_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_comentario', to=settings.AUTH_USER_MODEL),
        ),
    ]