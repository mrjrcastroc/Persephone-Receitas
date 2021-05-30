# Generated by Django 3.1.2 on 2020-10-25 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0005_usuario_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_cadastrado', to=settings.AUTH_USER_MODEL),
        ),
    ]