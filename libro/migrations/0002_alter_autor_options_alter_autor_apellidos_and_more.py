# Generated by Django 4.1.3 on 2022-11-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='apellidos',
            field=models.CharField(max_length=220, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.CharField(max_length=600, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=100, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombres'),
        ),
    ]
