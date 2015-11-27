# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.CharField(max_length=8)),
                ('sexo', models.CharField(blank=True, max_length=255, verbose_name=b'G\xc3\xa9nero', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=13)),
                ('estado', models.BooleanField(default=True)),
                ('imagen', models.ImageField(upload_to=b'perfiles')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rol', models.CharField(unique=True, max_length=20)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='perfiles',
            name='rol',
            field=models.ForeignKey(to='perfiles.Rol'),
        ),
        migrations.AddField(
            model_name='perfiles',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accesos',
            name='direccion',
            field=models.ForeignKey(to='perfiles.Direcion'),
        ),
        migrations.AddField(
            model_name='accesos',
            name='rol',
            field=models.ForeignKey(to='perfiles.Rol'),
        ),
    ]
