# Generated by Django 3.1.2 on 2020-10-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0003_auto_20201026_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='denunciareceita',
            name='resolvida',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='denunciareceita',
            name='situacao',
            field=models.CharField(default='em analise', max_length=200),
            preserve_default=False,
        ),
    ]
