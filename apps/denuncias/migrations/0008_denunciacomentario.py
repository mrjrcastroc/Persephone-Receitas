# Generated by Django 3.1.2 on 2020-11-11 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0004_auto_20201025_0000'),
        ('receitas', '0030_auto_20201110_1141'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('denuncias', '0007_auto_20201110_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='DenunciaComentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('texto', models.TextField()),
                ('data_denuncia', models.DateField(auto_now_add=True)),
                ('situacao', models.CharField(blank=True, max_length=200)),
                ('resolvida', models.BooleanField(default=False)),
                ('categoria_denuncia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_denuncia_c', to='denuncias.categoriadenuncia')),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denuncia_comentarios', to='comentarios.comentarios')),
                ('receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receita_comentario', to='receitas.receita')),
                ('usuario_denunciado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_denunciado_por_comentario', to=settings.AUTH_USER_MODEL)),
                ('usuario_efetuou_denuncia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_efetuou_denuncia_comentario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
